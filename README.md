# Formosana

臺灣本土語言相關資料整理。

## 檔案說明

### 音節表

- `臺灣台語羅馬字拼音方案音節表_table.md` — 整理為 Markdown 表格的音節表，以聲母為欄、韻母為列，含台灣語假名標註

### 教育部資料 (`docs_MOE/`)

- `臺灣台語羅馬字拼音方案音節表_1130826.pdf` — 教育部公告之臺灣台語羅馬字拼音方案音節表（1130826 修訂版）原始 PDF
- `臺灣台語羅馬字拼音方案音節表_1130826.md` — 從 PDF 轉出的純文字版本
- `臺灣台語羅馬字拼音方案使用手冊.pdf` — 教育部公告之使用手冊原始 PDF
- `臺灣台語羅馬字拼音方案使用手冊.md` — 從 PDF 轉出的純文字版本
- `kautian.ods` — 教育部臺灣台語常用詞辭典資料（ODS 格式）
- `kautian_*.csv` — 從 `kautian.ods` 各工作表匯出的 CSV 檔

## 工具

- `docs_MOE/parse_tailo.py` — 將純文字版音節表（`_1130826.md`）解析並轉換為 Markdown 表格。執行方式：
  ```
  python3 docs_MOE/parse_tailo.py > 臺灣台語羅馬字拼音方案音節表_table.md
  ```
- `ods2csv.py` — 將 ODS 檔轉換為 CSV，每個工作表一個檔案。執行方式：
  ```
  python3 ods2csv.py docs_MOE/kautian.ods
  ```
- `extract_pairs.py` — 從 `kautian_詞目.csv` 擷取羅馬字、漢字配對。執行方式：
  ```
  python3 extract_pairs.py                                    # 輸出至終端
  python3 extract_pairs.py docs_MOE/kautian_詞目.csv out.csv  # 輸出至 CSV
  ```
