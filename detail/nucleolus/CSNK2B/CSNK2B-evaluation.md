---
type: protein-evaluation
gene: "CSNK2B"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CSNK2B 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CSNK2B / CK2N, G5A |
| 蛋白名称 | Casein kinase II subunit beta |
| 蛋白大小 | 215 aa / 24.9 kDa |
| UniProt ID | P67870 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nucleoli fibrillar center, Perinuclear thec; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 215 aa / 24.9 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=76 篇 (≤80→4) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=93.6; PDB: 1DS5, 1JWH, 1QF8, 3EED, 4DGL, 4MD7, 4MD8 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR016149, IPR035991, IPR000704; Pfam: PF01214 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **116.0/180** | |
| **归一化总分** | | | **64.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoli fibrillar center, Perinuclear theca, Calyx, Mid piece | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像获取**: 未下载本地IF图像（standard evaluation），核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- extracellular region (GO:0005576)
- fibrillar center (GO:0001650)
- ficolin-1-rich granule lumen (GO:1904813)
- nucleoplasm (GO:0005654)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 76 |
| PubMed broad count | 104 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CK2N, G5A |

**关键文献**:
1. CSNK2B: A broad spectrum of neurodevelopmental disability and epilepsy severity.. *Epilepsia*. PMID: 34041744
2. Integrated molecular analysis of adult T cell leukemia/lymphoma.. *Nature genetics*. PMID: 26437031
3. Activating Transcription Factor 6 Mediates Inflammatory Signals in Intestinal Epithelial Cells Upon Endoplasmic Reticulum Stress.. *Gastroenterology*. PMID: 32673694
4. CSNK2 suppresses autophagy by activating FLN-NHL-containing TRIM proteins.. *Autophagy*. PMID: 37938186
5. Pathogenic missense variants of CSNK2B associated with Poirier-Bienvenu neurodevelopmental disorder impact differently on CK2 holoenzyme formation.. *Biological chemistry*. PMID: 40317201

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 93.6 |
| 高置信度残基 (pLDDT>90) 占比 | 87.0% |
| 置信残基 (pLDDT 70-90) 占比 | 6.5% |
| 中等置信 (pLDDT 50-70) 占比 | 5.6% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 93.5% |
| 可用 PDB 条目 | 1DS5, 1JWH, 1QF8, 3EED, 4DGL, 4MD7, 4MD8, 4MD9, 4NH1, 6Q38 |

**PAE**: PAE 图像未生成本地文件（standard evaluation），结构判断基于 AlphaFold pLDDT 统计。

**评价**: PDB实验结构（1DS5, 1JWH, 1QF8, 3EED, 4DGL, 4MD7, 4MD8, 4MD9, 4NH1, 6Q38）+ AlphaFold极高置信度预测（pLDDT=93.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR016149, IPR035991, IPR000704; Pfam: PF01214 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CSNK2A2 | 0.999 | 0.958 | — |
| CSNK2A1 | 0.999 | 0.999 | — |
| CSNK2A3 | 0.967 | 0.505 | — |
| NFKBIA | 0.964 | 0.620 | — |
| RYBP | 0.964 | 0.795 | — |
| PCGF5 | 0.961 | 0.837 | — |
| CTNNB1 | 0.955 | 0.058 | — |
| RRP7A | 0.944 | 0.572 | — |
| SSRP1 | 0.943 | 0.873 | — |
| DVL2 | 0.940 | 0.162 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000415303.2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| CSNK2A2 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| LYN | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| CSNK2A1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| ZNHIT1 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| RPL5 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| MBD4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| ZNF44 | psi-mi:"MI:0018"(two hybrid) | pubmed:14667819|mint:MINT-5216 |
| Ppp2r1a | psi-mi:"MI:0091"(chromatography technology) | pubmed:16857963|imex:IM-19330 |
| COIL | psi-mi:"MI:0018"(two hybrid) | pubmed:16713569|imex:IM-11827| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=93.6 + PDB: 1DS5, 1JWH, 1QF8, 3EED, 4DGL,  | pLDDT=93.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm; 额外: Nucleoli fibrillar center, Perinu | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CSNK2B — Casein kinase II subunit beta，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小215 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 76 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P67870
- Protein Atlas: https://www.proteinatlas.org/ENSG00000204435-CSNK2B/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CSNK2B
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P67870
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
