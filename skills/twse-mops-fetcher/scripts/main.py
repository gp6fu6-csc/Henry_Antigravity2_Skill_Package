import os
import argparse
from mops_downloader import fetch_and_organize_reports
from pdf_parser import export_extracted_tables
from gemini_analyzer import generate_financial_analysis_report

def main():
    parser = argparse.ArgumentParser(description="公開資訊觀測站 (TWSE MOPS) 資料擷取與財報分析 Skill")
    parser.add_argument("--stock", type=str, required=True, help="股票代號（多檔請用逗號分隔，例如 4195,2330）")
    parser.add_argument("--year", type=str, required=True, help="民國年份（例如 114）")
    parser.add_argument("--type", type=str, default="財務報告書", help="資料種類（預設：財務報告書）")
    parser.add_argument("--outdir", type=str, default="g:/我的雲端硬碟/股市研究", help="電腦指定下載路徑")
    parser.add_argument("--analyze", action="store_true", help="是否自動進行 PDF 表格解析與 Gemini 財報分析")

    args = parser.parse_args()

    stock_list = [s.strip() for s in args.stock.split(",") if s.strip()]
    year = args.year.strip()
    outdir = os.path.abspath(args.outdir)

    print("=" * 60)
    print("🚀 公開資訊觀測站 (TWSE MOPS) 自動化資料擷取 Skill 啟動")
    print(f"📌 目標股票代號: {stock_list}")
    print(f"📌 民國年份: {year}")
    print(f"📌 資料種類: {args.type}")
    print(f"📌 儲存路徑: {outdir}")
    print(f"📌 Gemini 財報分析: {'開啟' if args.analyze else '關閉'}")
    print("=" * 60)

    total_downloaded = []

    for stock in stock_list:
        print(f"\n>>> 正在處理股票 {stock}...")
        downloaded = fetch_and_organize_reports(
            stock_code=stock,
            year=year,
            output_base_dir=outdir,
            data_type=args.type
        )
        total_downloaded.extend(downloaded)

        if args.analyze and downloaded:
            print(f"\n[*] 正在對股票 {stock} 下載之 PDF 執行解析與 Gemini 分析...")
            for pdf_file in downloaded:
                try:
                    export_extracted_tables(pdf_file)
                    generate_financial_analysis_report(pdf_file)
                except Exception as e:
                    print(f"[ERROR] 解析或生成分析報告失敗 ({pdf_file}): {e}")

    print("\n" + "=" * 60)
    print(f"🎉 任務完成！共下載 {len(total_downloaded)} 個檔案。")
    for filepath in total_downloaded:
        print(f"  📄 [PDF] {filepath}")
    print("=" * 60)

if __name__ == "__main__":
    main()
