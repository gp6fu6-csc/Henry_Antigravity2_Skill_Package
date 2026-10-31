import os
import re
import time
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Optional

DOC_SERVER_URL = "https://doc.twse.com.tw/server-java/t57sb01"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-TW,zh;q=0.9,en-US;q=0.8,en;q=0.7",
}

def query_financial_reports(stock_code: str, year: str) -> List[Dict[str, str]]:
    """
    查詢指定股票代號與民國年份的財務報告書。
    POST 至 doc.twse.com.tw/server-java/t57sb01 (step=1)
    """
    payload = {
        "step": "1",
        "colorchg": "1",
        "co_id": str(stock_code).strip(),
        "year": str(year).strip(),
        "mtype": "A"
    }

    try:
        resp = requests.post(DOC_SERVER_URL, data=payload, headers=HEADERS, timeout=15)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        results = []
        # Find <a> tags containing javascript:readfile2 or readfile
        links = soup.find_all('a')
        for link in links:
            href = link.get('href', '')
            text = link.get_text(strip=True)
            
            # Pattern: javascript:readfile2("A","4195","202502_4195_AI1.pdf");
            match = re.search(r"readfile2?\(\s*[\"'](.*?)[\"']\s*,\s*[\"'](.*?)[\"']\s*,\s*[\"'](.*?)[\"']\s*\)", href)
            if match:
                kind, coid, filename = match.groups()
                results.append({
                    "stock_code": coid,
                    "year": year,
                    "kind": kind,
                    "filename": filename,
                    "display_name": text
                })
        return results
    except Exception as e:
        print(f"[ERROR] 查詢 MOPS (doc.twse.com.tw) 失敗: {e}")
        return []

def get_pdf_download_url(kind: str, stock_code: str, filename: str) -> Optional[str]:
    """
    對 doc.twse.com.tw POST step=9 取得動態 PDF 下載連結。
    """
    payload = {
        "step": "9",
        "kind": kind,
        "co_id": stock_code,
        "filename": filename
    }
    try:
        resp = requests.post(DOC_SERVER_URL, data=payload, headers=HEADERS, timeout=15)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'html.parser')
        
        a_tag = soup.find('a')
        if a_tag and a_tag.get('href'):
            href = a_tag.get('href')
            pdf_url = href if href.startswith('http') else "https://doc.twse.com.tw" + href
            return pdf_url
        return None
    except Exception as e:
        print(f"[ERROR] 取得 PDF 下載網址失敗 ({filename}): {e}")
        return None

def download_file(url: str, save_path: str) -> bool:
    """
    下載指定 URL 的檔案並儲存至 save_path。
    """
    try:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        resp = requests.get(url, headers=HEADERS, stream=True, timeout=30)
        if resp.status_code == 200:
            with open(save_path, 'wb') as f:
                for chunk in resp.iter_content(chunk_size=8192):
                    f.write(chunk)
            print(f"[SUCCESS] 下載成功: {save_path}")
            return True
        else:
            print(f"[ERROR] 下載失敗 (HTTP {resp.status_code}): {url}")
            return False
    except Exception as e:
        print(f"[ERROR] 下載例外: {e}")
        return False

def fetch_and_organize_reports(
    stock_code: str,
    year: str,
    output_base_dir: str = "g:/我的雲端硬碟/股市研究",
    data_type: str = "財務報告書"
) -> List[str]:
    """
    完整下載流程：
    目錄結構: <output_base_dir>/<stock_code>/<data_type>/
    檔名規則: <stock_code>_<year>年_<filename>
    """
    print(f"[*] 正在查詢股票 {stock_code} 民國 {year} 年的 {data_type}...")
    target_dir = os.path.join(output_base_dir, stock_code, data_type)
    os.makedirs(target_dir, exist_ok=True)
    
    downloaded_files = []
    reports = query_financial_reports(stock_code, year)
    print(f"[*] 找到 {len(reports)} 個可下載的 PDF 檔案資訊。")
    
    for item in reports:
        kind = item["kind"]
        coid = item["stock_code"]
        fname = item["filename"]
        
        pdf_url = get_pdf_download_url(kind, coid, fname)
        if pdf_url:
            save_name = f"{stock_code}_{year}年_{fname}"
            save_path = os.path.join(target_dir, save_name)
            if download_file(pdf_url, save_path):
                downloaded_files.append(save_path)
            time.sleep(1) # Friendly delay
            
    return downloaded_files

if __name__ == "__main__":
    import sys
    stock = sys.argv[1] if len(sys.argv) > 1 else "4195"
    yr = sys.argv[2] if len(sys.argv) > 2 else "114"
    files = fetch_and_organize_reports(stock, yr)
    print(f"\n[SUMMARY] 共下載 {len(files)} 個檔案。")
