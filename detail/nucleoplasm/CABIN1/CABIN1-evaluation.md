---
type: protein-evaluation
gene: "CABIN1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CABIN1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CABIN1 / KIAA0330 |
| 蛋白名称 | Calcineurin-binding protein cabin-1 |
| 蛋白大小 | 2220 aa / 246.4 kDa |
| UniProt ID | Q9Y6J0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Nucleus |
| 蛋白大小 | 2/10 | ×1 | 2 | 2220 aa / 246.4 kDa |
| 研究新颖性 | 6/10 | ×5 | 30 | PubMed strict=57 篇 (≤60→6) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=63.7; PDB: 1N6J |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033053, IPR015134, IPR011990, IPR019734; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **102.5/180** | |
| **归一化总分** | | | **56.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- aggresome (GO:0016235)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小偏离理想范围，实验设计需特殊考虑。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 57 |
| PubMed broad count | 138 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0330 |

**关键文献**:
1. Phosphorylation and ubiquitination-dependent degradation of CABIN1 releases p53 for transactivation upon genotoxic stress.. *Nucleic acids research*. PMID: 23303793
2. Cabin1 localizes in glomerular podocyte and undergoes nuclear translocation during podocyte injury.. *Renal failure*. PMID: 26275115
3. Knocking down Cabin1 induces glomerular podocyte injury.. *International urology and nephrology*. PMID: 29368245
4. Cabin1 restrains p53 activity on chromatin.. *Nature structural & molecular biology*. PMID: 19668210
5. CABIN1 peptide effectively targets MEF2D-fusion protein in B-cell precursor acute lymphoblastic leukemia.. *Signal transduction and targeted therapy*. PMID: 40947444

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 63.7 |
| 高置信度残基 (pLDDT>90) 占比 | 23.0% |
| 置信残基 (pLDDT 70-90) 占比 | 30.5% |
| 中等置信 (pLDDT 50-70) 占比 | 6.7% |
| 低置信 (pLDDT<50) 占比 | 39.8% |
| 有序区域 (pLDDT>70) 占比 | 53.5% |
| 可用 PDB 条目 | 1N6J |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=63.7），有序残基占 53.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033053, IPR015134, IPR011990, IPR019734; Pfam: PF09047 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HIRA | 0.999 | 0.835 | — |
| UBN1 | 0.999 | 0.817 | — |
| ASF1A | 0.998 | 0.820 | — |
| MEF2B | 0.996 | 0.973 | — |
| MEF2D | 0.940 | 0.625 | — |
| UBN2 | 0.872 | 0.236 | — |
| CALML5 | 0.868 | 0.227 | — |
| ASF1B | 0.850 | 0.735 | — |
| CALM3 | 0.849 | 0.075 | — |
| CALML4 | 0.842 | 0.075 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| - | psi-mi:"MI:0096"(pull down) | pubmed:19505873|imex:IM-20483 |
| Pou5f1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:20362542|imex:IM-16970 |
| Tfcp2l1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20362541|imex:IM-16928 |
| MEF2B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| H1-1 | psi-mi:"MI:0030"(cross-linking study) | pubmed:30021884|imex:IM-26653| |
| M | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-27674|pubmed:33208464 |
| ASF1B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CDX1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| EAF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| XAGE1A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=63.7 + PDB: 1N6J | pLDDT=63.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CABIN1 — Calcineurin-binding protein cabin-1，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小2220 aa，大小偏离理想范围，实验设计需特殊考虑。

**风险/不确定性**:
1. PubMed 57 篇，已有一定研究基础
2. AlphaFold 预测质量一般（pLDDT=63.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y6J0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000099991-CABIN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CABIN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y6J0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
