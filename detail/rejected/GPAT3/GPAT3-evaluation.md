---
type: protein-evaluation
gene: "GPAT3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## GPAT3 — REJECTED (核定位证据不足 (核定位得分 2/10 ≤ 3))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | GPAT3 / AGPAT9, MAG1 |
| 蛋白名称 | Glycerol-3-phosphate acyltransferase 3 |
| 蛋白大小 | 434 aa / 48.7 kDa |
| UniProt ID | Q53EU6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 2/10 | ×4 | 8 | HPA: 暂无HPA定位数据; UniProt: Endoplasmic reticulum membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 434 aa / 48.7 kDa |
| 研究新颖性 | 4/10 | ×5 | 20 | PubMed strict=65 篇 (≤80→4) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=85.3; PDB: 无 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045252, IPR002123; Pfam: PF01553 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **88.5/180** | |
| **归一化总分** | | | **49.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum membrane (GO:0005789)

**结论**: 核定位证据极弱，主要数据源均不指向细胞核。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 65 |
| PubMed broad count | 113 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AGPAT9, MAG1 |

**关键文献**:
1. GPAT3 regulates the synthesis of lipid intermediate LPA and exacerbates Kupffer cell inflammation mediated by the ERK signaling pathway.. *Cell death & disease*. PMID: 36964139
2. Glycerol-3-phosphate acyltransferase 3-mediated lipid droplets accumulation confers chemoresistance of colorectal cancer.. *MedComm*. PMID: 38344398
3. CHP1 promotes lipid droplet growth and regulates the localization of key enzymes for triacylglycerol synthesis.. *Proceedings of the National Academy of Sciences of the United States of America*. PMID: 40875810
4. Oligomers of the lipodystrophy protein seipin may co-ordinate GPAT3 and AGPAT2 enzymes to facilitate adipocyte differentiation.. *Scientific reports*. PMID: 32094408
5. Multi-omics characterization of type 2 diabetes mellitus-induced gastroenteropathy in the db/db mouse model.. *Frontiers in cell and developmental biology*. PMID: 39211388

**评价**: 已有一定研究基础，但仍存在niche空间。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 85.3 |
| 高置信度残基 (pLDDT>90) 占比 | 47.9% |
| 置信残基 (pLDDT 70-90) 占比 | 41.5% |
| 中等置信 (pLDDT 50-70) 占比 | 7.6% |
| 低置信 (pLDDT<50) 占比 | 3.0% |
| 有序区域 (pLDDT>70) 占比 | 89.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=85.3，有序区 89.4%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045252, IPR002123; Pfam: PF01553 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GPAM | 0.995 | 0.000 | — |
| GPAT2 | 0.983 | 0.000 | — |
| GPD1L | 0.943 | 0.000 | — |
| GPD1 | 0.942 | 0.000 | — |
| GK | 0.941 | 0.049 | — |
| GK2 | 0.939 | 0.049 | — |
| GPD2 | 0.928 | 0.000 | — |
| AGK | 0.914 | 0.000 | — |
| AGPAT2 | 0.911 | 0.000 | — |
| GPAT4 | 0.903 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CANX | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |
| SLC6A15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TCTN3 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| TMEM216 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| TCTN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| TMEM17 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| KLRD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| TSPAN15 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| KCNK1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| GPR182 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=85.3 + PDB: 无 | pLDDT=85.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Endoplasmic reticulum membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. GPAT3 — Glycerol-3-phosphate acyltransferase 3，已有一定研究基础，但仍存在niche空间。
2. 蛋白大小434 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 65 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
- [ ] **该蛋白核定位证据不足（≤3/10），不建议作为核蛋白研究目标。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q53EU6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000138678-GPAT3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=GPAT3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q53EU6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q53EU6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
