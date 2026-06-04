---
type: protein-evaluation
gene: "TYSND1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TYSND1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TYSND1 |
| 蛋白名称 | Peroxisomal leader peptide-processing protease |
| 蛋白大小 | 566 aa / 59.3 kDa |
| UniProt ID | Q2T9J0 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nucleoplasm, Centrosome; 额外: Cytosol; UniProt: Peroxisome |
| 蛋白大小 | 10/10 | ×1 | 10 | 566 aa / 59.3 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=10 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=83.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017345, IPR009003, IPR039245; Pfam: PF13365 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Centrosome; 额外: Cytosol | Uncertain |
| UniProt | Peroxisome | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytosol (GO:0005829)
- membrane (GO:0016020)
- peroxisomal matrix (GO:0005782)
- peroxisome (GO:0005777)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 10 |
| PubMed broad count | 10 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Identification of potential candidate genes for the Huoyan trait in developing Wulong goose embryos by transcriptomic analysis.. *British poultry science*. PMID: 38727584
2. Identification of Peroxisomal Protein Complexes with PTS Receptors, Pex5 and Pex7, in Mammalian Cells.. *Sub-cellular biochemistry*. PMID: 30378028
3. Depletion of LONP2 unmasks differential requirements for peroxisomal function between cell types and in cholesterol metabolism.. *Biology direct*. PMID: 37736739
4. Two proteases, trypsin domain-containing 1 (Tysnd1) and peroxisomal lon protease (PsLon), cooperatively regulate fatty acid β-oxidation in peroxisomal matrix.. *The Journal of biological chemistry*. PMID: 22002062
5. Novel peroxisomal protease Tysnd1 processes PTS1- and PTS2-containing enzymes involved in beta-oxidation of fatty acids.. *The EMBO journal*. PMID: 17255948

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 83.4 |
| 高置信度残基 (pLDDT>90) 占比 | 55.5% |
| 置信残基 (pLDDT 70-90) 占比 | 26.7% |
| 中等置信 (pLDDT 50-70) 占比 | 9.5% |
| 低置信 (pLDDT<50) 占比 | 8.3% |
| 有序区域 (pLDDT>70) 占比 | 82.2% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 中等质量（pLDDT=83.4，有序区 82.2%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017345, IPR009003, IPR039245; Pfam: PF13365 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ACOX1 | 0.960 | 0.292 | — |
| ACAA1 | 0.956 | 0.000 | — |
| LONP2 | 0.898 | 0.292 | — |
| PEX5 | 0.891 | 0.525 | — |
| AGPS | 0.881 | 0.211 | — |
| HSD17B4 | 0.864 | 0.292 | — |
| SCP2 | 0.860 | 0.292 | — |
| PHYH | 0.849 | 0.000 | — |
| PEX14 | 0.789 | 0.000 | — |
| PEX7 | 0.774 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000287078.6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22002062|imex:IM-17176 |
| CAT | psi-mi:"MI:0663"(confocal microscopy) | pubmed:22002062|imex:IM-17176 |
| PEX5 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:22002062|imex:IM-17176 |
| gag-pol | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| EBI-6248077 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-17346|pubmed:22190034| |
| JOSD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| TEKT3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HSPA8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ANKRD40 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| STUB1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=83.4 + PDB: 无 | pLDDT=83.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome / Nucleoplasm, Centrosome; 额外: Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. TYSND1 — Peroxisomal leader peptide-processing protease，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小566 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 10 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q2T9J0
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156521-TYSND1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TYSND1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2T9J0
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
