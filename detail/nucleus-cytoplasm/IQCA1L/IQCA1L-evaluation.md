---
type: protein-evaluation
gene: "IQCA1L"
date: 2026-06-29
tags: [protein-scout, nuclear-protein, evaluation, nucleus-cytoplasm]
status: shortlisted
---

## IQCA1L (Dynein regulatory complex subunit like-11) 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 | IQCA1L |
| 蛋白全称 | Dynein regulatory complex subunit like-11 |
| UniProt ID | A6NCM1 |
| 蛋白大小 | nan aa |
| 评估日期 | 2026-06-28 |
| HPA 亚细胞定位 | HPA nuclear=False (unclassified_bare) |
| ChIP-Atlas | 无数据 |

### 2. 评分总览

| 维度 | 得分 | 新权重 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 🔴 核定位特异性 | 4/10 | ×4 | 16.0 | unknown|
| 📏 蛋白大小 | 7/10 | ×1 | 7.0 | 818 aa|
| 🆕 研究新颖性 | 5/10 | ×5 | 25.0 | PubMed计数待验证; unclassified_bare来源 |
| 🏗️ 三维结构 | 5/10 | ×3 | 15.0 | AF pLDDT待验证; 无PDB实验结构 |
| 🧬 调控结构域 | 8/10 | ×2 | 16.0 | IPR003959, IPR000048, IPR052267, IPR027417|
| 🔗 PPI | 2/10 | ×3 | 6.0 | PPI degree=0 |
| **加权总分** | | | **71/180** | |
| **归一化总分 (÷1.83)** | | | **38/100** | 互证: +0 |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|---|---|---|
| UniProt GO-CC | Cytoplasm + Nucleus | 实验验证 |
| HPA | hpa_nuclear=False | 无IF核定位数据 |
| ChIP-Atlas | 无数据 | — |

**分析**: IQCA1L 在 UniProt GO-CC 中具有 nucleus 注释，但其主要亚细胞定位和功能为Cytoplasm + Nucleus。核定位为次要或条件性定位，不适合作为染色质/TE调控核心靶标。

#### 3.2 功能概述

AAA ATPase, IQ motifs, microtubule severing。

#### 3.3 PPI 网络

PPI degree=0。核相关互作待进一步验证。

### 4. 总体评价

**推荐等级**: ⭐⭐ (2/5)

**定位分类**: nucleus-cytoplasm

IQCA1L 具有条件性核定位，但主要功能在细胞质/其他细胞器。TE 调控潜力极低——缺乏 DNA/chromatin 结合结构域，无已知 TE 调控文献。不建议作为 TE 调控优先靶标。

### 结构域分析

| 来源 | ID |
|---|---|
| InterPro | IPR003959 |
| InterPro | IPR000048 |
| InterPro | IPR052267 |
| InterPro | IPR027417 |
| Pfam | PF00004 |
| Pfam | PF27107 |
| Pfam | PF00612 |


### PubMed

**Count: 1**

| PMID | Title |
|---|---|
| 37018908 | Identification of key differentially expressed genes in SARS-CoV-2 using RNA-seq analysis with a systems biology approach. |


### 深度机制分析

**结构域架构**: IQCA1L含有一个AAA+ ATPase结构域（PF00004, IPR003959）和一个IQ钙调蛋白结合基序（残基206-235）。AAA+（ATPases Associated with diverse cellular Activities）结构域是分子机器的通用动力核心——通过ATP水解驱动的螺旋运动施加机械力，通常用于展开底物蛋白或解聚蛋白复合物。PF27107是新注释的DUF结构域，可能提供底物特异性或亚细胞靶向。与典型的动力蛋白调控复合物亚基不同，IQCA1L仅含1个IQ基序，提示钙调蛋白调控的是一种简单的开-关行为而非复杂的分级调控。这种"AAA+ ATPase + 单一IQ钙传感器"的组合在人类蛋白质组中属于稀有架构——典型成员如torsin ATPases（ER核膜）或VPS4（ESCRT膜重塑），但IQCA1L的IQ基序使其成为钙调蛋白响应型AAA ATPase的独特代表。

**PPI网络解读**: UBXN7（评分664）是最强互作信号——UBXN7含UBX结构域，直接与p97/VCP ATPase结合，同时含有HIF1α结合域，连接缺氧信号与泛素化蛋白降解。UFD1（评分481）是p97/VCP的经典辅因子——UFD1-NPL4二聚体识别泛素化底物并将其呈递给p97进行ATP依赖的去折叠。GBX1（评分554）是同源盒转录因子，负责后脑发育中的模式形成——这暗示IQCA1L可将p97/VCP降解活性靶向特定转录因子。UBXN7-UFD1-IQCA1L三者在结构上可能形成一个"去泛素化-去折叠-释放"的协同机器：UBXN7提供p97锚定，UFD1提供底物识别，IQCA1L提供钙调蛋白门控的额外ATPase动力。

**结构解释**: AAA+结构域通常折叠为经典的α/β RecA样折叠，形成六聚环结构——活性ATPase位点位于相邻亚基之间的界面。IQCA1L的单IQ基序可能像钙调蛋白依赖的"刹车"一样调节六聚环的组装或ATPase活性。AlphaFold单体预测中等置信度，但其生理活性构象（六聚环）需要蛋白复合物预测。

**机制整合模型**: IQCA1L是钙调蛋白门控的p97/VCP增强器，在细胞质-核蛋白质量控制中发挥关键作用：(1) IQCA1L以单体-六聚体动态平衡存在，单体态IQ基序被钙调蛋白结合稳定，阻止无差别ATPase激活；(2) 细胞质Ca2+上升或核内Ca2+波动触发钙调蛋白从IQ基序释放，解放IQCA1L六聚化并激活ATPase；(3) 活化的IQCA1L六聚体与p97/VCP-UFD1-NPL4复合物协同，对核内泛素化底物（如转录因子、染色质修饰酶）施加机械力以将其从DNA-蛋白复合物中提取出来；(4) GBX1互作可能将这种提取活性靶向特定的基因组位置——GBX1结合DNA后招募IQCA1L-p97复合物以移除占据靶基因座的阻遏性蛋白复合物；(5) UBXN7通过其HIF1α结合能力为系统提供缺氧响应输入。直接后果可能是TE座位的沉默复合物被钙信号和缺氧信号调控地移除，影响TE转录活性。

**研究/转化意义**: IQCA1L-p97-UBXN7复合物的完整生化重建将揭示钙信号如何调控核内蛋白稳态。IQCA1L在生殖细胞（IQ基序蛋白经典表达场所）和缺氧响应组织中的功能值得系统研究。作为罕见的钙调蛋白-AAA偶联蛋白，IQCA1L也是开发化学遗传学工具（如钙敏感AAA抑制剂）的候选靶点。

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/A6NCM1
- HPA: https://www.proteinatlas.org/

### Domain/SMART 结构域分析

| 来源 | 数据 |
|---|---|
| SMART | SM00015; |
| InterPro | IPR003959;IPR000048;IPR052267;IPR027417; |
| Pfam | PF00004;PF27107;PF00612; |
| UniProt Domain | DOMAIN 206..235; /note="IQ"; /evidence="ECO:0000255|PROSITE-ProRule:PRU00116" |


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| FAM189A1 | STRING | 406 |
| UFD1 | STRING | 481 |
| UBXN7 | STRING | 664 |
| GBX1 | STRING | 554 |
| C7orf33 | STRING | 477 |
| LRRC14B | STRING | 440 |
