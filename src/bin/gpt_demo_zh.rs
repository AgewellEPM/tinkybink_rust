//! 🇨🇳 中文GPT演示 - 智能AAC系统
//!
//! 展示中文GPT核心的强大功能：
//! - 自然中文语言处理
//! - 文化情感感知
//! - 中文会话模式
//! - 训练数据集成

use anyhow::Result;
use colored::*;
use serde_json::Value;
use std::fs;
use std::io::{self, Write};
use std::path::Path;
use tinkybink_rust::ai::gpt_core_zh::{GPT配置, 中文GPT核心, 情感状态};

/// 中文训练数据加载器
struct 中文数据加载器 {
    词汇表: Vec<String>,
    句子集: Vec<Vec<String>>,
    情感集: Vec<情感状态>,
}

impl 中文数据加载器 {
    fn 新建() -> Result<Self> {
        let mut 词汇表 = Vec::new();
        let mut 句子集 = Vec::new();
        let mut 情感集 = Vec::new();

        // 加载所有中文训练文件
        let 训练目录 = Path::new("training_zh");
        if 训练目录.exists() {
            for 条目 in fs::read_dir(训练目录)? {
                let 条目 = 条目?;
                let 路径 = 条目.path();
                if 路径.extension().and_then(|s| s.to_str()) == Some("json") {
                    let 内容 = fs::read_to_string(&路径)?;
                    let 数据: Value = serde_json::from_str(&内容)?;

                    if let Some(节点) = 数据["nodes"].as_array() {
                        for 节点项 in 节点 {
                            // 提取文本
                            if let Some(文本) = 节点项["text"].as_str() {
                                let 字符: Vec<String> = 文本.chars().map(|c| c.to_string()).collect();
                                句子集.push(字符.clone());
                                for 字 in 字符 {
                                    if !词汇表.contains(&字) {
                                        词汇表.push(字);
                                    }
                                }
                            }

                            // 提取情感
                            if let Some(情感) = 节点项["emotion"].as_object() {
                                let 状态 = 情感状态 {
                                    价值性: 情感.get("价值性").and_then(|v| v.as_f64()).unwrap_or(0.5) as f32,
                                    激活度: 情感.get("激活度").and_then(|v| v.as_f64()).unwrap_or(0.5) as f32,
                                    主导性: 情感.get("主导性").and_then(|v| v.as_f64()).unwrap_or(0.3) as f32,
                                    含蓄度: 情感.get("含蓄度").and_then(|v| v.as_f64()).unwrap_or(0.7) as f32,
                                    和谐性: 情感.get("和谐性").and_then(|v| v.as_f64()).unwrap_or(0.8) as f32,
                                };
                                情感集.push(状态);
                            }
                        }
                    }
                }
            }
        }

        // 如果没有数据，使用默认示例
        if 词汇表.is_empty() {
            let 默认词汇 = vec![
                "你", "好", "早", "上", "晚", "再", "见", "谢", "谢", "我", "很", "开", "心", "难", "过", "饿", "了",
                "渴", "想", "睡", "觉", "妈", "爸", "老", "师", "同", "学", "吃", "饭", "喝", "水", "玩", "游", "戏",
                "回", "家", "学", "校", "作", "业", "休", "息", "加", "油", "对", "不", "起", "没", "关", "系", "请",
                "帮", "助", "疼", "救", "命", "医", "生", "爱", "喜", "欢", "害", "怕",
            ];
            词汇表 = 默认词汇.iter().map(|s| s.to_string()).collect();
        }

        Ok(Self { 词汇表, 句子集, 情感集 })
    }

    fn 分词(&self, 文本: &str) -> Vec<usize> {
        文本
            .chars()
            .filter_map(|字符| {
                let 字符串 = 字符.to_string();
                self.词汇表.iter().position(|v| v == &字符串)
            })
            .collect()
    }

    fn 组词(&self, 令牌: &[usize]) -> String {
        令牌.iter().filter_map(|&索引| self.词汇表.get(索引)).cloned().collect::<Vec<_>>().join("")
    }
}

/// 主演示函数
fn 运行演示() -> Result<()> {
    println!("{}", "╔══════════════════════════════════════════════════════════╗".cyan());
    println!("{}", "║      🇨🇳 TINKYBINK 中文GPT - 智能AAC系统      ║".cyan().bold());
    println!("{}", "╚══════════════════════════════════════════════════════════╝".cyan());
    println!();

    // 加载训练数据
    println!("{} 加载中文训练数据...", "→".green());
    let 加载器 = 中文数据加载器::新建()?;
    println!("{} 词汇量：{} 个字符", "✓".green(), 加载器.词汇表.len());
    println!("{} 训练句子：{} 句", "✓".green(), 加载器.句子集.len());
    println!("{} 情感状态：{} 个", "✓".green(), 加载器.情感集.len());
    println!();

    // 配置模型
    let 配置 = GPT配置 {
        词汇量大小: 加载器.词汇表.len().max(1000),
        隐藏层维度: 256,
        层数: 6,
        注意力头数: 8,
        上下文长度: 512,
        dropout率: 0.1,
        情感温度: 0.6,
    };

    println!("{} 初始化中文GPT核心...", "→".yellow());
    let mut 模型 = 中文GPT核心::新建(配置);
    println!("{} 模型准备就绪！", "✓".green().bold());
    println!();

    // 演示菜单
    loop {
        println!("{}", "┌─────────────────────────────────────┐".magenta());
        println!("{}", "│           演示菜单                   │".magenta().bold());
        println!("{}", "├─────────────────────────────────────┤".magenta());
        println!("{}", "│ 1. 生成中文问候                      │".magenta());
        println!("{}", "│ 2. 表达基本需求                      │".magenta());
        println!("{}", "│ 3. 展示文化情感                      │".magenta());
        println!("{}", "│ 4. 互动对话                          │".magenta());
        println!("{}", "│ 5. 和谐表达演示                      │".magenta());
        println!("{}", "│ 6. 紧急情况                          │".magenta());
        println!("{}", "│ 0. 退出                              │".magenta());
        println!("{}", "└─────────────────────────────────────┘".magenta());

        print!("\n{} 请选择选项：", "→".cyan());
        io::stdout().flush()?;

        let mut 输入 = String::new();
        io::stdin().read_line(&mut 输入)?;

        match 输入.trim() {
            "1" => 演示问候(&mut 模型, &加载器)?,
            "2" => 演示需求(&mut 模型, &加载器)?,
            "3" => 演示情感(&mut 模型, &加载器)?,
            "4" => 互动对话(&mut 模型, &加载器)?,
            "5" => 演示和谐(&mut 模型, &加载器)?,
            "6" => 演示紧急(&mut 模型, &加载器)?,
            "0" => {
                println!("\n{} 再见！祝您一切顺利！", "👋".to_string().yellow());
                break;
            }
            _ => println!("{} 无效选项", "✗".red()),
        }

        println!();
    }

    Ok(())
}

fn 演示问候(模型: &mut 中文GPT核心, 加载器: &中文数据加载器) -> Result<()> {
    println!("\n{}", "=== 中文问候生成 ===".green().bold());

    // 设置友好和谐的情感状态
    模型.更新情感(情感状态 { 价值性: 0.9, 激活度: 0.6, 主导性: 0.4, 含蓄度: 0.6, 和谐性: 0.9 });

    let 提示词 = vec!["你好", "早上", "晚上"];

    for 提示 in 提示词 {
        let 令牌 = 加载器.分词(提示);
        if !令牌.is_empty() {
            let 生成 = 模型.生成(&令牌, 5)?;
            let 文本 = 加载器.组词(&生成);
            println!("{} {} → {}", "💬".to_string(), 提示.yellow(), 文本.green());
        }
    }

    Ok(())
}

fn 演示需求(模型: &mut 中文GPT核心, 加载器: &中文数据加载器) -> Result<()> {
    println!("\n{}", "=== 基本需求表达 ===".blue().bold());

    // 需求状态的情感
    模型.更新情感(情感状态 { 价值性: 0.4, 激活度: 0.7, 主导性: 0.5, 含蓄度: 0.5, 和谐性: 0.7 });

    let 需求词 = vec!["我饿", "我渴", "我想"];

    for 需求 in 需求词 {
        let 令牌 = 加载器.分词(需求);
        if !令牌.is_empty() {
            let 生成 = 模型.生成(&令牌, 4)?;
            let 文本 = 加载器.组词(&生成);
            println!("{} {} → {}", "🆘".to_string(), 需求.yellow(), 文本.cyan());
        }
    }

    Ok(())
}

fn 演示情感(模型: &mut 中文GPT核心, 加载器: &中文数据加载器) -> Result<()> {
    println!("\n{}", "=== 文化情感表达 ===".magenta().bold());

    let 情感列表 = vec![
        ("开心", 情感状态 { 价值性: 0.9, 激活度: 0.7, 主导性: 0.5, 含蓄度: 0.6, 和谐性: 0.9 }, "😊"),
        ("难过", 情感状态 { 价值性: 0.2, 激活度: 0.3, 主导性: 0.2, 含蓄度: 0.8, 和谐性: 0.6 }, "😢"),
        ("和谐", 情感状态 { 价值性: 0.8, 激活度: 0.5, 主导性: 0.5, 含蓄度: 0.7, 和谐性: 1.0 }, "☮️"),
    ];

    for (名称, 情感, 表情) in 情感列表 {
        模型.更新情感(情感);
        let 令牌 = 加载器.分词("我");
        if !令牌.is_empty() {
            let 生成 = 模型.生成(&令牌, 6)?;
            let 文本 = 加载器.组词(&生成);
            println!("{} {} → {}", 表情, 名称.yellow(), 文本.magenta());
        }
    }

    Ok(())
}

fn 互动对话(模型: &mut 中文GPT核心, 加载器: &中文数据加载器) -> Result<()> {
    println!("\n{}", "=== 互动对话 ===".cyan().bold());
    println!("{}", "请输入中文（输入'退出'结束）".italic());

    loop {
        print!("\n{} 您：", "👤".to_string());
        io::stdout().flush()?;

        let mut 输入 = String::new();
        io::stdin().read_line(&mut 输入)?;
        let 输入 = 输入.trim();

        if 输入 == "退出" {
            break;
        }

        // 分析输入情感
        let 情感 = 分析输入情感(输入);
        模型.更新情感(情感);

        let 令牌 = 加载器.分词(输入);
        if !令牌.is_empty() {
            let 生成 = 模型.生成(&令牌, 8)?;
            let 回复 = 加载器.组词(&生成);
            println!("{} TinkyBink：{}", "🤖".to_string(), 回复.green());
        } else {
            println!("{} TinkyBink：{}", "🤖".to_string(), "不好意思，请再说一遍".yellow());
        }
    }

    Ok(())
}

fn 演示和谐(模型: &mut 中文GPT核心, 加载器: &中文数据加载器) -> Result<()> {
    println!("\n{}", "=== 和谐表达演示 ===".green().bold());

    // 最大和谐与含蓄
    模型.更新情感(情感状态 { 价值性: 0.8, 激活度: 0.5, 主导性: 0.3, 含蓄度: 0.9, 和谐性: 1.0 });

    let 表达 = vec!["谢谢", "对不起", "没关系"];

    for 词语 in 表达 {
        let 令牌 = 加载器.分词(词语);
        if !令牌.is_empty() {
            let 生成 = 模型.生成(&令牌, 6)?;
            let 文本 = 加载器.组词(&生成);
            println!("{} {} → {}", "🕊️".to_string(), 词语.green(), 文本.yellow());
        }
    }

    Ok(())
}

fn 演示紧急(模型: &mut 中文GPT核心, 加载器: &中文数据加载器) -> Result<()> {
    println!("\n{}", "=== 紧急情况 ===".red().bold().on_yellow());

    // 紧急状态
    模型.更新情感(情感状态 {
        价值性: 0.1,
        激活度: 1.0,
        主导性: 0.3,
        含蓄度: 0.2, // 紧急时不含蓄
        和谐性: 0.5,
    });

    let 紧急词 = vec!["救命", "我疼", "叫医生"];

    for 紧急 in 紧急词 {
        let 令牌 = 加载器.分词(紧急);
        if !令牌.is_empty() {
            let 生成 = 模型.生成(&令牌, 5)?;
            let 文本 = 加载器.组词(&生成);
            println!("{} {} → {}", "🚨".to_string(), 紧急.red().bold(), 文本.on_red().white());
        }
    }

    println!("\n{} 拨打120急救电话...", "📞".to_string().blink());

    Ok(())
}

fn 分析输入情感(文本: &str) -> 情感状态 {
    // 基础情感分析
    let 正面词 = ["开心", "好", "喜欢", "爱", "快乐", "高兴", "棒"];
    let 负面词 = ["难过", "不好", "疼", "害怕", "生气", "累"];
    let 紧急词 = ["救命", "紧急", "疼", "需要", "帮助"];
    let 和谐词 = ["谢谢", "请", "对不起", "没关系", "辛苦"];

    let mut 价值性: f32 = 0.5;
    let mut 激活度: f32 = 0.5;
    let mut 含蓄度: f32 = 0.7;
    let mut 和谐性: f32 = 0.8;

    for 词 in 正面词.iter() {
        if 文本.contains(词) {
            价值性 += 0.2;
            激活度 += 0.1;
        }
    }

    for 词 in 负面词.iter() {
        if 文本.contains(词) {
            价值性 -= 0.2;
            激活度 += 0.1;
        }
    }

    for 词 in 紧急词.iter() {
        if 文本.contains(词) {
            激活度 = 1.0;
            含蓄度 = 0.2;
        }
    }

    for 词 in 和谐词.iter() {
        if 文本.contains(词) {
            和谐性 = 1.0;
            含蓄度 = 0.8;
        }
    }

    // 感叹号减少含蓄度
    let 感叹号数 = 文本.matches('！').count() as f32;
    含蓄度 = (含蓄度 - 感叹号数 * 0.1).max(0.0);

    情感状态 {
        价值性: 价值性.clamp(0.0, 1.0),
        激活度: 激活度.clamp(0.0, 1.0),
        主导性: 0.5,
        含蓄度: 含蓄度.clamp(0.0, 1.0),
        和谐性: 和谐性.clamp(0.0, 1.0),
    }
}

fn main() {
    println!(
        "{}",
        "
╔═══════════════════════════════════════════════════════════════════╗
║                                                                    ║
║   ████████╗██╗███╗   ██╗██╗  ██╗██╗   ██╗██████╗ ██╗███╗   ██╗██╗  ██╗  ║
║   ╚══██╔══╝██║████╗  ██║██║ ██╔╝╚██╗ ██╔╝██╔══██╗██║████╗  ██║██║ ██╔╝  ║
║      ██║   ██║██╔██╗ ██║█████╔╝  ╚████╔╝ ██████╔╝██║██╔██╗ ██║█████╔╝   ║
║      ██║   ██║██║╚██╗██║██╔═██╗   ╚██╔╝  ██╔══██╗██║██║╚██╗██║██╔═██╗   ║
║      ██║   ██║██║ ╚████║██║  ██╗   ██║   ██████╔╝██║██║ ╚████║██║  ██╗  ║
║      ╚═╝   ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝   ╚═╝   ╚═════╝ ╚═╝╚═╝  ╚═══╝╚═╝  ╚═╝  ║
║                                                                    ║
║                  🇨🇳 中文GPT - 智能交流系统 🇨🇳                     ║
║                                                                    ║
╚═══════════════════════════════════════════════════════════════════╝
    "
        .bright_red()
        .bold()
    );

    if let Err(e) = 运行演示() {
        eprintln!("{} 错误：{}", "✗".red().bold(), e);
        std::process::exit(1);
    }
}
