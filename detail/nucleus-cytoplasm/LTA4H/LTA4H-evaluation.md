---
type: protein-evaluation
gene: "LTA4H"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## LTA4H — REJECTED (研究热度过高 (PubMed strict=277，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | LTA4H / LTA4 |
| 蛋白名称 | Leukotriene A-4 hydrolase |
| 蛋白大小 | 611 aa / 69.3 kDa |
| UniProt ID | P09960 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 611 aa / 69.3 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=277 篇 (>100→REJECTED) |
| 三维结构 | 4/10 | ×3 | 12 | AlphaFold v6 pLDDT=0; PDB: 1GW6, 1H19, 1HS6, 1SQM, 2R59, 2VJ8, 3B7R |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045357, IPR042097, IPR016024, IPR012777, IPR049 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **75.0/180** | |
| **归一化总分** | | | **41.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol; 额外: Nucleoplasm | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- ficolin-1-rich granule lumen (GO:1904813)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- tertiary granule lumen (GO:1904724)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 277 |
| PubMed broad count | 325 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: LTA4 |

**关键文献**:
1. LTA4H improves the tumor microenvironment and prevents HCC progression via targeting the HNRNPA1/LTBP1/TGF-β axis.. *Cell reports. Medicine*. PMID: 40056904
2. Neurotuberculosis: an update.. *Acta neurologica Belgica*. PMID: 33400226
3. Causal Role for Neutrophil Elastase in Thoracic Aortic Dissection in Mice.. *Arteriosclerosis, thrombosis, and vascular biology*. PMID: 37589142
4. Pharmacogenetics of asthma.. *Current opinion in pulmonary medicine*. PMID: 19077707
5. Down-regulating HDAC2-LTA4H pathway ameliorates renal ischemia-reperfusion injury.. *Biochimica et biophysica acta. Molecular basis of disease*. PMID: 40324735

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 0 |
| 高置信度残基 (pLDDT>90) 占比 | 0% |
| 置信残基 (pLDDT 70-90) 占比 | 0% |
| 中等置信 (pLDDT 50-70) 占比 | 0% |
| 低置信 (pLDDT<50) 占比 | 0% |
| 有序区域 (pLDDT>70) 占比 | 0% |
| 可用 PDB 条目 | 1GW6, 1H19, 1HS6, 1SQM, 2R59, 2VJ8, 3B7R, 3B7S, 3B7T, 3B7U |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=0），有序残基占 0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045357, IPR042097, IPR016024, IPR012777, IPR049980; Pfam: PF09127, PF01433, PF17900 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ALOX5 | 0.992 | 0.050 | — |
| LTC4S | 0.992 | 0.000 | — |
| ALOX5AP | 0.950 | 0.000 | — |
| CYP4F3 | 0.936 | 0.054 | — |
| CYP4F2 | 0.920 | 0.054 | — |
| LTB4R2 | 0.892 | 0.000 | — |
| TRIT1 | 0.886 | 0.000 | — |
| LTB4R | 0.842 | 0.000 | — |
| PLA2G2A | 0.745 | 0.000 | — |
| CYSLTR1 | 0.694 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMEM62 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ARPC3 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| HLA-C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MCC | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| GH1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| UBA5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| DDA1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| ENSP00000228740.2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=0 + PDB: 1GW6, 1H19, 1HS6, 1SQM, 2R59,  | pLDDT=0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm / Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. LTA4H — Leukotriene A-4 hydrolase，研究基础较多，新颖性有限。
2. 蛋白大小611 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 277 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=0），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 277 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P09960
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111144-LTA4H/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=LTA4H
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P09960
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
