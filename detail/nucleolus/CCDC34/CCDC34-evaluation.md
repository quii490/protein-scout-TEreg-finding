---
type: protein-evaluation
gene: "CCDC34"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CCDC34 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CCDC34 / RAMA3 |
| 蛋白名称 | Coiled-coil domain-containing protein 34 |
| 蛋白大小 | 373 aa / 43.2 kDa |
| UniProt ID | Q96HJ3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane, Nucleoli fibrillar center, Calyx, Mid piec; UniProt: Cell projection, cilium, flagellum |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 43.2 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=68.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR045323, IPR025259; Pfam: PF13904 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 9 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **118.0/180** | |
| **归一化总分** | | | **65.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Nucleoli fibrillar center, Calyx, Mid piece; 额外: Connecting piece, Principal piece, End piece | Approved |
| UniProt | Cell projection, cilium, flagellum | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- sperm midpiece (GO:0097225)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 20 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: RAMA3 |

**关键文献**:
1. CCDC34 maintains stemness phenotype through β-catenin-mediated autophagy and promotes EGFR-TKI resistance in lung adenocarcinoma.. *Cancer gene therapy*. PMID: 39587349
2. CCDC34 is up-regulated in bladder cancer and regulates bladder cancer cell proliferation, apoptosis and migration.. *Oncotarget*. PMID: 26312564
3. Up-Regulated CCDC34 Contributes to the Proliferation and Metastasis of Hepatocellular Carcinoma.. *OncoTargets and therapy*. PMID: 32021254
4. RABL2A-CCDC34 Axis Promotes Sorafenib Resistance in Hepatocellular Carcinoma.. *DNA and cell biology*. PMID: 34767735
5. Expression of Coiled-Coil Domain Containing 34 (CCDC34) and its Prognostic Significance in Pancreatic Adenocarcinoma.. *Medical science monitor : international medical journal of experimental and clinical research*. PMID: 29257799

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 68.9 |
| 高置信度残基 (pLDDT>90) 占比 | 35.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.5% |
| 中等置信 (pLDDT 50-70) 占比 | 27.6% |
| 低置信 (pLDDT<50) 占比 | 29.0% |
| 有序区域 (pLDDT>70) 占比 | 43.4% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=68.9），有序残基占 43.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045323, IPR025259; Pfam: PF13904 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| RABL2A | 0.708 | 0.637 | — |
| LGR4 | 0.641 | 0.045 | — |
| LIN7C | 0.626 | 0.000 | — |
| CCDC106 | 0.605 | 0.000 | — |
| CCDC150 | 0.549 | 0.000 | — |
| CCDC77 | 0.545 | 0.000 | — |
| DEPDC1B | 0.542 | 0.000 | — |
| FAM216A | 0.518 | 0.000 | — |
| RIBC2 | 0.509 | 0.125 | — |
| GSTCD | 0.488 | 0.081 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TMEM86B | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| COQ8A | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| RABL2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ACTBL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FAM76B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KAT5 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| SETDB1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| LMO3 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32814053|imex:IM-28217| |
| YWHAG | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:32814053|imex:IM-28217| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 9
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 9 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=68.9 + PDB: 无 | pLDDT=68.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cell projection, cilium, flagellum / Nuclear membrane, Nucleoli fibrillar center, Calyx | 一致 |
| PPI | STRING + IntAct | 15 + 9 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CCDC34 — Coiled-coil domain-containing protein 34，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. AlphaFold 预测质量一般（pLDDT=68.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96HJ3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000109881-CCDC34/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CCDC34
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96HJ3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
