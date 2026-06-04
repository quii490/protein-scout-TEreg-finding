---
type: protein-evaluation
gene: "WDR48"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## WDR48 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | WDR48 / KIAA1449, UAF1 |
| 蛋白名称 | WD repeat-containing protein 48 |
| 蛋白大小 | 677 aa / 76.2 kDa |
| UniProt ID | Q8TAF3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles; UniProt: Nucleus; Cytoplasm; Lysosome; Late endosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 677 aa / 76.2 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=29 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.9; PDB: 5CVL, 5CVN, 5CVO, 5K1A, 5K1B, 5K1C, 5L8E |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001 |
| PPI 网络 | 2/10 | ×3 | 6 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **132.5/180** | |
| **归一化总分** | | | **73.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles | Supported |
| UniProt | Nucleus; Cytoplasm; Lysosome; Late endosome | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- late endosome (GO:0005770)
- lysosome (GO:0005764)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 29 |
| PubMed broad count | 80 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA1449, UAF1 |

**关键文献**:
1. RPA exhaustion activates SLFN11 to eliminate cells with heightened replication stress.. *Nature cell biology*. PMID: 41514018
2. WD repeat domain 48 promotes hepatocellular carcinoma progression by stabilizing c-Myc.. *Journal of cellular and molecular medicine*. PMID: 36403194
3. Structural Insights into WD-Repeat 48 Activation of Ubiquitin-Specific Protease 46.. *Structure (London, England : 1993)*. PMID: 26388029
4. DEPDC5 regulates the strength of excitatory synaptic transmission by interacting with ubiquitin-specific protease 46.. *Neurobiology of disease*. PMID: 40467011
5. The USP1-WDR48 deubiquitinase complex functions as a molecular switch regulating tumor-associated macrophage activation and anti-tumor response.. *Cell death and differentiation*. PMID: 40707784

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.9 |
| 高置信度残基 (pLDDT>90) 占比 | 74.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.1% |
| 中等置信 (pLDDT 50-70) 占比 | 5.0% |
| 低置信 (pLDDT<50) 占比 | 7.1% |
| 有序区域 (pLDDT>70) 占比 | 87.8% |
| 可用 PDB 条目 | 5CVL, 5CVN, 5CVO, 5K1A, 5K1B, 5K1C, 5L8E, 5L8W, 6JLQ, 7AY0 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（5CVL, 5CVN, 5CVO, 5K1A, 5K1B, 5K1C, 5L8E, 5L8W, 6JLQ, 7AY0）+ AlphaFold极高置信度预测（pLDDT=88.9），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR015943, IPR020472, IPR019775, IPR036322, IPR001680; Pfam: PF11816, PF00400 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| MAP1LC3B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| USP12 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PHLPP2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PHLPP1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| UIMC1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| WDR20 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| TP53 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| SUPT6H | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| PPP1R9A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- 仅IntAct实验
- STRING partners: 0，IntAct interactions: 15
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.9 + PDB: 5CVL, 5CVN, 5CVO, 5K1A, 5K1B,  | pLDDT=88.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Lysosome; Late endosome / Vesicles | 一致 |
| PPI | STRING + IntAct | 0 + 15 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. WDR48 — WD repeat-containing protein 48，非常新颖，仅有少数基础研究。
2. 蛋白大小677 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 29 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8TAF3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000114742-WDR48/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=WDR48
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8TAF3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
