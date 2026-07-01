---
type: protein-evaluation
gene: "POFUT3"
uniprot: "Q6P4F1"
date: 2026-06-28
tags: [protein-scout, nucleus-cytoplasm, evaluation, rejected]
status: rejected
---

## POFUT3 / Protein O-Fucosyltransferase 3 评估报告

### 1. 基本信息
| 项目 | 内容 |
|---|---|
| 基因名 | POFUT3 (别名: FUT10) |
| 蛋白全称 | GDP-fucose protein O-fucosyltransferase 3 |
| UniProt ID | Q6P4F1 (Swiss-Prot, reviewed) |
| 蛋白大小 | 479 aa |
| UniProt 证据等级 | 1: Evidence at protein level |
| 亚细胞定位 | **Endoplasmic reticulum membrane; Golgi apparatus membrane** (单次跨膜蛋白) |

### 2. 评分总览
| 维度 | 得分 | 权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 0/10 | x4 | 0.0 | ER/Golgi 膜蛋白; 非核定位 |
| 蛋白大小 | 6/10 | x1 | 6.0 | 479 aa |
| 新颖性 | 4/10 | x5 | 20.0 | PubMed=19; hotness=6 |
| 三维结构 | 2/10 | x3 | 6.0 | Glycosyltransferase family 10 fold |
| 调控结构域 | 0/10 | x2 | 0.0 | 糖基转移酶催化域; 无染色质/DNA结合域 |
| PPI | 2/10 | x3 | 6.0 | PPI degree=0 (BioGRID: 12弱连接) |
| **加权总分** | | | **38.0/180** | |
| **归一化总分** | | | **21.1/100** | |

### 3. 详细分析

**核定位: 完全不成立 (FAIL)**。POFUT3 是一个**内质网 (ER) 膜蛋白**和**高尔基体膜蛋白**，UniProt 定位为 "Endoplasmic reticulum membrane; Single-pass type II membrane protein"。该蛋白的 N 端位于胞质侧，催化域位于 ER 腔内，专门负责在分泌途径中的蛋白质上进行 O-岩藻糖基化修饰。**该蛋白不可能存在于细胞核中**。

**功能**: POFUT3 催化 EMI 结构域中丝氨酸/苏氨酸残基的 O-岩藻糖基化，底物包括 MMRN1、MMRN2 和 EMID1 (PMID: 39775168)。此修饰可能促进蛋白质折叠和分泌。属于 glycosyltransferase family 10，含 7 种可变剪接异构体。

**关键点**: 这不是一个核蛋白。糖基转移酶在 ER/Golgi 中进行翻译后修饰，与染色质、转录调控或 TE 沉默无关。催化域为 UDP-glycosyltransferase/glycogen phosphorylase fold — 这是一个糖基转移催化结构域，与 DNA 结合或组蛋白修饰没有任何结构或功能关联。

**PPI 网络**: PPI degree=0 (从筛选数据) 或 BioGRID 中的 12 条弱连接 — 这些相互作用主要是糖基转移酶底物识别相关，不涉及任何核蛋白或染色质因子。

**TE 调控潜力**: **零**。POFUT3 是分泌途径中的糖基转移酶，参与胞外蛋白的翻译后修饰。它在生物学上完全定位于 ER/Golgi 的膜系统，与细胞核、染色质或 TE 沉默无关。

### 4. 总体评价
**21.1/100** | **REJECTED**

**拒绝理由**: POFUT3 是一个**ER/Golgi 膜定位的糖基转移酶**，与染色质和转录调控完全无关。其在筛选数据中获得 tier=2 和 hotness=6 可能来源于序列中富含半胱氨酸的 EMI 底物识别模块被误判为核蛋白特征。该蛋白不含任何核定位信号、DNA 结合域或染色质相关模块。Genecards 条目中存在 mouse symbol "Pofut3" 混入的问题。

**关键文献**:
- 39775168: POFUT3 催化 EMI 结构域 O-fucosylation
- 19088067: Alpha-(1,3)-fucosyltransferase 活性 (in vivo 活性不确定)
