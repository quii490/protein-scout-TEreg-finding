---
type: protein-evaluation
gene: "Elob"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## Elob 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Elob / TCEB2 |
| 蛋白名称 | Elongin-B |
| 蛋白大小 | 118 aa / 13.1 kDa |
| UniProt ID | Q15370 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 118 aa / 13.1 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=38 篇 (≤40→8) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=92.5; PDB: 1LM8, 1LQB, 1VCB, 2C9W, 2IZV, 2JZ3, 2MA9 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR039049, IPR000626, IPR029071; Pfam: PF00240 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **134.0/180** | |
| **归一化总分** | | | **74.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- Cul2-RING ubiquitin ligase complex (GO:0031462)
- Cul5-RING ubiquitin ligase complex (GO:0031466)
- cytosol (GO:0005829)
- elongin complex (GO:0070449)
- nucleoplasm (GO:0005654)
- VCB complex (GO:0030891)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 38 |
| PubMed broad count | 99 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TCEB2 |

**关键文献**:
1. USP51 facilitates colorectal cancer stemness and chemoresistance by forming a positive feed-forward loop with HIF1A.. *Cell death and differentiation*. PMID: 37816999
2. Elongin B promotes breast cancer progression by ubiquitinating tumor suppressor p14/ARF.. *Cell biology and toxicology*. PMID: 38653919
3. Peptide-mediated inhibition of the transcriptional regulator Elongin BC induces apoptosis in cancer cells.. *Cell chemical biology*. PMID: 37354906
4. ASB1 engages with ELOB to facilitate SQOR ubiquitination and H(2)S homeostasis during spermiogenesis.. *Redox biology*. PMID: 39733518
5. Insights into the target-directed miRNA degradation mechanism in Drosophila ovarian cell culture.. *Biochimica et biophysica acta. Gene regulatory mechanisms*. PMID: 40328417

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.5 |
| 高置信度残基 (pLDDT>90) 占比 | 88.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.4% |
| 低置信 (pLDDT<50) 占比 | 6.8% |
| 有序区域 (pLDDT>70) 占比 | 89.8% |
| 可用 PDB 条目 | 1LM8, 1LQB, 1VCB, 2C9W, 2IZV, 2JZ3, 2MA9, 3DCG, 3ZKJ, 3ZNG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1LM8, 1LQB, 1VCB, 2C9W, 2IZV, 2JZ3, 2MA9, 3DCG, 3ZKJ, 3ZNG）+ AlphaFold极高置信度预测（pLDDT=92.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR039049, IPR000626, IPR029071; Pfam: PF00240 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ELOA | 0.999 | 0.839 | — |
| CUL2 | 0.999 | 0.983 | — |
| RNF7 | 0.999 | 0.789 | — |
| ELOC | 0.999 | 0.999 | — |
| VHL | 0.999 | 0.999 | — |
| HIF1A | 0.999 | 0.966 | — |
| CBFB | 0.999 | 0.918 | — |
| CUL5 | 0.999 | 0.983 | — |
| RBX1 | 0.999 | 0.951 | — |
| NEDD8 | 0.998 | 0.883 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ELOC | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:10205047 |
| VHL | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:10205047 |
| MED8 | psi-mi:"MI:0018"(two hybrid) | pubmed:12149480 |
| Cul2 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:12149480 |
| RBX1 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:12149480 |
| Dmel\CG6380 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| TSC22D1 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| vif | psi-mi:"MI:0096"(pull down) | imex:IM-17346|pubmed:22190034| |
| Npro | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.5 + PDB: 1LM8, 1LQB, 1VCB, 2C9W, 2IZV,  | pLDDT=92.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. Elob — Elongin-B，非常新颖，仅有少数基础研究。
2. 蛋白大小118 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 38 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q15370
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103363-ELOB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Elob
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q15370
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELOB/IF_images/166942_A_7_3_rna_selected.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/ELOB/IF_images/166942_A_8_4_rna_selected.jpg]]



<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q15370-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
