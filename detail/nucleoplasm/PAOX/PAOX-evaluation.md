---
type: protein-evaluation
gene: "PAOX"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## PAOX 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PAOX / PAO |
| 蛋白名称 | Peroxisomal N(1)-acetyl-spermine/spermidine oxidase |
| 蛋白大小 | 511 aa / 55.5 kDa |
| UniProt ID | Q6QHF9 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Centrosome; 额外: Nucleoplasm; UniProt: Peroxisome; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 511 aa / 55.5 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=35 篇 (≤40→8) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=92.4; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR002937, IPR036188, IPR050281; Pfam: PF01593 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 1 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.5/180** | |
| **归一化总分** | | | **64.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Centrosome; 额外: Nucleoplasm | Uncertain |
| UniProt | Peroxisome; Cytoplasm | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- peroxisomal matrix (GO:0005782)

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 35 |
| PubMed broad count | 81 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAO |

**关键文献**:
1. Biosynthesis, herbivore induction, and defensive role of phenylacetaldoxime glucoside.. *Plant physiology*. PMID: 37584327
2. Gene polymorphisms of SFTPB rs7316, rs9752 and PAOX rs1046175 affect the diagnostic value of plasma Pro-SFTPB and DAS in Chinese Han non-small-cell lung cancer patients.. *Journal of cellular biochemistry*. PMID: 31016788
3. Expression of Polyamine Oxidase in Fibroblasts Induces MMP-1 and Decreases the Integrity of Extracellular Matrix.. *International journal of molecular sciences*. PMID: 36142401
4. Changes in seminal plasma microecological dynamics and the mechanistic impact of core metabolite hexadecanamide in asthenozoospermia patients.. *iMeta*. PMID: 38882497
5. Polyamine Oxidase Expression Is Downregulated by 17β-Estradiol via Estrogen Receptor 2 in Human MCF-7 Breast Cancer Cells.. *International journal of molecular sciences*. PMID: 35886868

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.4 |
| 高置信度残基 (pLDDT>90) 占比 | 84.1% |
| 置信残基 (pLDDT 70-90) 占比 | 9.8% |
| 中等置信 (pLDDT 50-70) 占比 | 2.5% |
| 低置信 (pLDDT<50) 占比 | 3.5% |
| 有序区域 (pLDDT>70) 占比 | 93.9% |
| 可用 PDB 条目 | 无 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=92.4，有序区 93.9%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR002937, IPR036188, IPR050281; Pfam: PF01593 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SAT1 | 0.987 | 0.000 | — |
| SAT2 | 0.895 | 0.000 | — |
| SMS | 0.837 | 0.000 | — |
| SRM | 0.820 | 0.000 | — |
| ODC1 | 0.810 | 0.000 | — |
| GLYATL1 | 0.762 | 0.000 | — |
| AOC1 | 0.712 | 0.000 | — |
| AZIN2 | 0.704 | 0.000 | — |
| TYSND1 | 0.661 | 0.000 | — |
| ACOX1 | 0.653 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG8032 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 1
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 1 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.4 + PDB: 无 | pLDDT=92.4, v6 | 仅预测 |
| 定位 | UniProt + HPA | Peroxisome; Cytoplasm / Centrosome; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 1 interactions | 数据充分 |

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
1. PAOX — Peroxisomal N(1)-acetyl-spermine/spermidine oxidase，非常新颖，仅有少数基础研究。
2. 蛋白大小511 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 35 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6QHF9
- Protein Atlas: https://www.proteinatlas.org/ENSG00000148832-PAOX/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PAOX
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6QHF9
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
