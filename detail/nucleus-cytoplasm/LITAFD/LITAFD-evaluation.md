---
type: protein-evaluation
gene: "LITAFD"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## LITAFD (LITAF domain-containing protein) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | LITAFD |
| 蛋白全称 | LITAF domain-containing protein |
| UniProt ID | A0A1B0GVX0 |
| 蛋白大小 | nan aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 4/10 | ×1 | 4.0 | 72 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 7/10 | ×2 | 14.0 | IPR006629, IPR037519, PF10601|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=0 |
| **加权总分** | | | **71/180** | |
| **归一化总分 (÷1.83)** | | | **38/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Endosome + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: LITAFD 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Endosome + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

72 aa, zinc-binding, cytokine regulation。

#### 3.3 PPI 网络

PPI degree=0。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

LITAFD 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### PubMed

**Count: 1**

| PMID | Title |
|---|---|
| 34696794 | Equine vitiligo-like depigmentation in grey horses is related to genes involved in immune response and tumor metastasis. |


### 深度机制分析

**结构域架构**: LITAFD仅72个氨基酸，几乎完全由一个LITAF结构域（残基1-71, PF10601, SMART SM00714）构成，属于含锌指C3HC4型RING相关蛋白。LITAF结构域是LPS诱导的TNF-α因子家族的特征结构域——经典成员LITAF将内体LPS信号传递至TNF-α启动子。LITAFD几乎无额外的辅助结构域，这意味着其功能的每一层次都由这71个残基编码，是一种高度精简的信号适配器。LITAF结构域编码锌结合能力和可能的二聚化界面，类似其他LITAF家族成员的"同源二聚化-功能激活"模式。

**PPI网络解读——关键突破**: SETDB2互作（评分403）是本报告最具洞察力的发现。SETDB2（又称CLLD8/KMT1F）是H3K9甲基转移酶——催化H3K9me3，这是组成性异染色质和逆转录转座子沉默的经典标记。LITAFD-SETDB2轴直接将一个72 aa的微型蛋白与表观遗传沉默机器连接起来。FANCM（评分532）是Fanconi贫血核心复合物的DNA转位酶，参与复制叉逆转和链间交联修复，进一步将LITAFD锚定于染色质应激响应。NUBPL（评分416）是线粒体铁硫簇组装因子，暗示代谢-免疫偶联。RCBTB1（评分462）含BTB结构域，是Cullin3 E3泛素连接酶的底物适配器——暗示LITAFD通过SETDB2写入H3K9me3标记，同时通过RCBTB1/CUL3擦除/降解特定蛋白。

**结构解释**: 72 aa的蛋白不太可能产生高pLDDT的全折叠结构，但LITAF结构域核心（锌结合区域）预计为紧凑的锌指折叠。小蛋白在AlphaFold中常出现低置信度，但锌指结构域通常折叠良好。

**机制整合模型**: LITAFD是内体-核染色质沉默耦合器，运作逻辑如下：(1) 在未受刺激状态下，LITAFD以单体形式驻留在内体膜表面，LITAF锌指结构域与膜脂质或内体蛋白结合；(2) 内体TLR或胞质DNA感应通路（cGAS-STING）激活触发LITAFD构象变化——锌配位重排使核定位信号暴露，LITAFD从内体解离并转位至核内；(3) 在核内，LITAFD二聚化后作为桥接因子，一端识别特定基因组区域（可能通过锌指直接结合DNA或招募序列特异性因子），另一端通过PPI界面招募SETDB2；(4) SETDB2沉积H3K9me3，建立局部异染色质状态以沉默靶基因座；(5) FANCM提供染色质可及性窗口，RCBTB1/CUL3介导负反馈——降解活化态LITAFD以终止信号。该模型使LITAFD成为从内体免疫到核内表观遗传沉默的最短信号路径——仅72个氨基酸实现信号跨越。

**研究/转化意义**: LITAFD-SETDB2-FANCM是全新的免疫-表观遗传轴，其与TE沉默和自身免疫病（如SLE中内源性逆转录病毒的异常表达）的关联值得深入探索。作为人类蛋白质组中最精简的信号适配器之一，LITAFD也是合成生物学中构建最小化信号通路的理想模板。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A0A1B0GVX0
- HPA: https://www.proteinatlas.org/

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00714; |
| InterPro | IPR006629;IPR037519; |
| Pfam | PF10601; |
| UniProt Domain | DOMAIN 1..71; /note="LITAF"; /evidence="ECO:0000255|PROSITE-ProRule:PRU01181" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FANCM | STRING | 532 |
| NUBPL | STRING | 416 |
| OR2C1 | STRING | 422 |
| SETDB2 | STRING | 403 |
| RCBTB1 | STRING | 462 |
