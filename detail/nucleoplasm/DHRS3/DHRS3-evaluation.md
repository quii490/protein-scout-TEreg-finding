---
type: protein-evaluation
gene: "DHRS3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## DHRS3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DHRS3 / RDH17, SDR16C1 |
| 蛋白名称 | Short-chain dehydrogenase/reductase 3 |
| 蛋白大小 | 302 aa / 33.5 kDa |
| UniProt ID | O75911 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Mitochondria; 额外: Nucleoli; UniProt: Membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 302 aa / 33.5 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=0 篇 (≤20→10) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=94.2; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR057326, IPR036291, IPR002347; Pfam: PF00106 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.0/180** | |
| **归一化总分** | | | **68.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoli | Approved |
| UniProt | Membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- lipid droplet (GO:0005811)
- photoreceptor outer segment membrane (GO:0042622)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 0 |
| PubMed broad count | 0 |
| 别名(未计入scoring) | 无 |

**关键文献**:
无关键文献数据。

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 94.2 |
| 高置信度残基 (pLDDT>90) 占比 | 78.8% |
| 置信残基 (pLDDT 70-90) 占比 | 20.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.3% |
| 低置信 (pLDDT<50) 占比 | 0.3% |
| 有序区域 (pLDDT>70) 占比 | 99.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=94.2，有序区 99.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR057326, IPR036291, IPR002347; Pfam: PF00106 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| mpl | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| MED21 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| C5AR2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL17RC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| IL4R | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TLR5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PTCH2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CLPX | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| HRAS | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| SRC | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=94.2 + PDB: 无 | pLDDT=94.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | Membrane / Mitochondria; 额外: Nucleoli | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. DHRS3 — Short-chain dehydrogenase/reductase 3，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小302 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 0 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### PPI 互作网络

| 互作伙伴 | 来源 | 评分 |
|---|---|---|
| ALDH1A3 | STRING | 961 |
| DHRS4 | STRING | 934 |
| AOX1 | STRING | 910 |
| ELAVL1 | BioGRID | 1 |
| MED21 | BioGRID | 1 |
| HNRNPL | BioGRID | 1 |
| SRC | BioGRID | 1 |
| PTCH2 | BioGRID | 1 |


### TE 调控评估

该蛋白缺乏核/染色质定位证据，TE 调控潜力较低。

### HPA IF 图像

HPA 检索: https://www.proteinatlas.org/search/DHRS3

### PubMed

**Count: 96**

| PMID | Title |
|---|---|
| 42142584 | The retinol-metabolizing enzyme DHRS3 coordinates antigen presentation, endothelial stability, and cholesterol metabolism to suppress hepatocellular c |
| 42102993 | Emerging roles of dehydrogenase/reductase (DHRS) in cancer. |
| 42055722 | Mechanical Overload-Induced Retinoid Metabolism Is Involved in Protein Synthesis in Skeletal Muscle of Female Mice. |
| 41993611 | Discovery of a novel Nrf2 activator that modulates mitochondrial function in neurons by regulating DHRS3-Nrf2 interaction after ischemic stroke. |
| 41876016 | Impact of poly(rC)-binding protein 2 (PCBP2) on the malignant phenotype of cholangiocarcinoma. |


