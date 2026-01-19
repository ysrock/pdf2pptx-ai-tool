"""
使用 Gemini 3 Flash Preview 分析股票题材共性
"""
import json
import google.generativeai as genai

# 配置 API Key
API_KEY = "AIzaSyDbfm7TO6PhQmVAZfuwXrm7PlD19FwwAjs"
genai.configure(api_key=API_KEY)

# 图片中的股票代码和名称
target_stocks = {
    "300567": "精测电子",
    "300757": "罗博特科",
    "301205": "联特科技",
    "688200": "华峰测控",
    "688676": "金盘科技",
    "301629": "矽电股份",
    "688120": "华海清科",
    "688172": "燕东微",
    "301286": "侨源股份",
    "688147": "微导纳米",
    "301550": "斯菱股份",
    "002028": "思源电气",
    "688720": "艾森股份",
    "300331": "苏大维格",
    "301200": "大族数控",
    "688652": "京仪装备",
    "688603": "天承科技",
    "688401": "路维光电",
    "301075": "多瑞医药",
    "688525": "佰维存储",
    "688362": "甬矽电子",
    "688778": "厦钨新能",
    "688019": "安集科技",
    "688082": "盛美上海",
    "688661": "和林微纳",
    "603308": "应流股份",
    "605358": "立昂微",
    "600584": "长电科技",
}

def load_stock_data(jsonl_file):
    """从JSONL文件加载股票数据"""
    found_stocks = {}
    
    with open(jsonl_file, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line.strip())
                company_name = data.get('company', '')
                
                for code, name in target_stocks.items():
                    if name == company_name:
                        found_stocks[code] = {
                            'name': name,
                            'data': data.get('data', {})
                        }
                        break
            except json.JSONDecodeError:
                continue
    
    return found_stocks

def analyze_with_gemini(stocks_data):
    """使用 Gemini 分析股票题材共性"""
    
    # 构建提示词
    prompt = """你是一位专业的A股市场分析师。以下是今日股票预警系统捕捉到的28只股票及其详细信息（JSON格式）。

请分析这些股票在题材上的共性，回答以下问题：

1. **主线题材**: 这些股票最核心的共同题材是什么？占比多少？
2. **细分领域**: 按产业链或细分领域分类，列出各类别包含的股票
3. **驱动事件**: 是否有共同的催化事件或消息面驱动？
4. **关联性分析**: 这些股票之间的产业链上下游关系是怎样的？
5. **投资启示**: 基于以上分析，对后续行情有什么判断？

请用中文回复，格式清晰，重点突出。

---

以下是股票数据：

"""
    
    # 添加股票数据
    for code, info in stocks_data.items():
        stock_json = {
            'code': code,
            'name': info['name'],
            'themes': info['data'].get('themes', []),
            'themes_raw': info['data'].get('themes_raw', []),
            'facts': info['data'].get('facts', [])[:3],  # 只取前3个facts以节省token
            'event': info['data'].get('event', {})
        }
        prompt += f"\n### {code} {info['name']}\n```json\n{json.dumps(stock_json, ensure_ascii=False, indent=2)}\n```\n"

    # 使用 gemini-3-flash-preview 模型
    model_name = 'gemini-3-flash-preview'
    print(f"正在调用 {model_name} 进行分析...")
    print("=" * 60)
    
    model = genai.GenerativeModel(model_name)
    response = model.generate_content(prompt)
    
    return response.text

def main():
    jsonl_file = r"c:\dev\data_basecreat\strict_v2_extracted.jsonl"
    
    print("正在加载股票数据...")
    stocks_data = load_stock_data(jsonl_file)
    print(f"找到 {len(stocks_data)} 只股票的数据")
    
    if not stocks_data:
        print("未找到任何股票数据，请检查JSONL文件")
        return
    
    # 调用 Gemini 分析
    result = analyze_with_gemini(stocks_data)
    
    print("\n" + "=" * 60)
    print("Gemini 分析结果:")
    print("=" * 60)
    print(result)
    
    # 保存结果
    output_file = r"c:\dev\data_basecreat\scripts\gemini_analysis_result.md"
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Gemini 股票题材共性分析\n\n")
        f.write(f"分析时间: 2026-01-16\n\n")
        f.write(f"分析股票数: {len(stocks_data)}\n\n")
        f.write("---\n\n")
        f.write(result)
    
    print(f"\n分析结果已保存到: {output_file}")

if __name__ == "__main__":
    main()
