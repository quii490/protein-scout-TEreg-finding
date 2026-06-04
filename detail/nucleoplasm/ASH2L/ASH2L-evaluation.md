---
type: protein-evaluation
gene: "ASH2L"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ASH2L — REJECTED (研究热度过高 (PubMed strict=148，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ASH2L / ASH2L1 |
| 蛋白名称 | Set1/Ash2 histone methyltransferase complex subunit ASH2 |
| 蛋白大小 | 628 aa / 68.7 kDa |
| UniProt ID | Q9UBL3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nucleoplasm; 额外: Plasma membrane; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 628 aa / 68.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=148 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.2; PDB: 3RSN, 3S32, 3TOJ, 4RIQ, 4X8N, 4X8P, 5F6K |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR037353, IPR049455, IPR053835, IPR001870, IPR043 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.0/180** | |
| **归一化总分** | | | **56.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Plasma membrane | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- histone methyltransferase complex (GO:0035097)
- MLL1 complex (GO:0071339)
- MLL1/2 complex (GO:0044665)
- MLL3/4 complex (GO:0044666)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- Set1C/COMPASS complex (GO:0048188)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 148 |
| PubMed broad count | 213 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: ASH2L1 |

**关键文献**:
1. ASH2L Deficiency in Smooth Muscle Drives Pulmonary Vascular Remodeling.. *Circulation research*. PMID: 39996311
2. ASH2L-K312-Lac Stimulates Angiogenesis in Tumors to Expedite the Malignant Progression of Hepatocellular Carcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40726441
3. Epigenetic-focused CRISPR/Cas9 screen identifies (absent, small, or homeotic)2-like protein (ASH2L) as a regulator of glioblastoma cell survival.. *Cell communication and signaling : CCS*. PMID: 37974198
4. Expression specificity and compensation effect of Ash2l-1/Ash2l-2 in mouse embryonic stem cells.. *Yi chuan = Hereditas*. PMID: 29576547
5. The Ash2l SDI Domain Is Required to Maintain the Stability and Binding of DPY30.. *Cells*. PMID: 35563756

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.2 |
| 高置信度残基 (pLDDT>90) 占比 | 50.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 4.3% |
| 低置信 (pLDDT<50) 占比 | 26.8% |
| 有序区域 (pLDDT>70) 占比 | 68.9% |
| 可用 PDB 条目 | 3RSN, 3S32, 3TOJ, 4RIQ, 4X8N, 4X8P, 5F6K, 5F6L, 6E2H, 6KIU |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（3RSN, 3S32, 3TOJ, 4RIQ, 4X8N, 4X8P, 5F6K, 5F6L, 6E2H, 6KIU）+ AlphaFold极高置信度预测（pLDDT=75.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR037353, IPR049455, IPR053835, IPR001870, IPR043136; Pfam: PF21198, PF21257, PF00622 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| KMT2A | 0.999 | 0.993 | — |
| CXXC1 | 0.999 | 0.994 | — |
| WDR82 | 0.999 | 0.928 | — |
| WDR5 | 0.999 | 0.995 | — |
| PAXIP1 | 0.999 | 0.839 | — |
| SETD1B | 0.999 | 0.978 | — |
| HCFC1 | 0.999 | 0.867 | — |
| SETD1A | 0.999 | 0.980 | — |
| RBBP5 | 0.999 | 0.997 | — |
| KMT2C | 0.999 | 0.989 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| DPY30 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HCFC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:12670868 |
| SIN3A | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:12670868 |
| SP1 | psi-mi:"MI:0029"(cosedimentation through density g | pubmed:12670868 |
| HCFC2 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15199122 |
| KMT2A | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15199122 |
| UNC119 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| ESR1 | psi-mi:"MI:0096"(pull down) | imex:IM-14474|pubmed:16603732 |
| KMT2D | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14474|pubmed:16603732 |
| RBBP5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-14474|pubmed:16603732 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.2 + PDB: 3RSN, 3S32, 3TOJ, 4RIQ, 4X8N,  | pLDDT=75.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Plasma membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. ASH2L — Set1/Ash2 histone methyltransferase complex subunit ASH2，研究基础较多，新颖性有限。
2. 蛋白大小628 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 148 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 148 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UBL3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129691-ASH2L/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ASH2L
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UBL3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
