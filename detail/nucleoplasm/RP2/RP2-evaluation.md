---
type: protein-evaluation
gene: "RP2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RP2 — REJECTED (研究热度过高 (PubMed strict=395，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RP2 |
| 蛋白名称 | Protein XRP2 |
| 蛋白大小 | 350 aa / 39.6 kDa |
| UniProt ID | O75695 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Mid piece, Principal piece, End piece; 额外: ; UniProt: Cell membrane; Cell projection, cilium |
| 蛋白大小 | 10/10 | ×1 | 10 | 350 aa / 39.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=395 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=92.0; PDB: 2BX6, 3BH6, 3BH7 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR017901, IPR016098, IPR036223, IPR006599, IPR036 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Mid piece, Principal piece, End piece; 额外: Nucleoplasm, Nuclear bodies, Vesicles, Cytosol, Acrosome | Approved |
| UniProt | Cell membrane; Cell projection, cilium | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- acrosomal vesicle (GO:0001669)
- centriole (GO:0005814)
- ciliary basal body (GO:0036064)
- cilium (GO:0005929)
- cytoplasm (GO:0005737)
- cytoplasmic vesicle (GO:0031410)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 395 |
| PubMed broad count | 1139 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Nonsyndromic Retinitis Pigmentosa Overview.. **. PMID: 20301590
2. The X-linked retinopathies: Physiological insights, pathogenic mechanisms, phenotypic features and novel therapies.. *Progress in retinal and eye research*. PMID: 32860923
3. Genetic and clinical findings in a Chinese cohort with Leber congenital amaurosis and early onset severe retinal dystrophy.. *The British journal of ophthalmology*. PMID: 31630094
4. Application of targeted panel sequencing and whole exome sequencing for 76 Chinese families with retinitis pigmentosa.. *Molecular genetics & genomic medicine*. PMID: 31960602
5. A multivesicular body-like organelle mediates stimulus-regulated trafficking of olfactory ciliary transduction proteins.. *Nature communications*. PMID: 36371422

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 92.0 |
| 高置信度残基 (pLDDT>90) 占比 | 86.9% |
| 置信残基 (pLDDT 70-90) 占比 | 3.7% |
| 中等置信 (pLDDT 50-70) 占比 | 4.0% |
| 低置信 (pLDDT<50) 占比 | 5.4% |
| 有序区域 (pLDDT>70) 占比 | 90.6% |
| 可用 PDB 条目 | 2BX6, 3BH6, 3BH7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（2BX6, 3BH6, 3BH7）+ AlphaFold高质量预测（pLDDT=92.0），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR017901, IPR016098, IPR036223, IPR006599, IPR036850; Pfam: PF07986 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ARL3 | 0.994 | 0.961 | — |
| UNC119B | 0.927 | 0.000 | — |
| NME9 | 0.647 | 0.048 | — |
| NME3 | 0.626 | 0.000 | — |
| NME6 | 0.623 | 0.000 | — |
| NME5 | 0.621 | 0.000 | — |
| NPHP3 | 0.593 | 0.000 | — |
| NME7 | 0.592 | 0.000 | — |
| NME1 | 0.583 | 0.000 | — |
| NME4 | 0.582 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=92.0 + PDB: 2BX6, 3BH6, 3BH7 | pLDDT=92.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, cilium / Plasma membrane, Mid piece, Principal piece, End p | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. RP2 — Protein XRP2，研究基础较多，新颖性有限。
2. 蛋白大小350 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 395 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 395 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75695
- Protein Atlas: https://www.proteinatlas.org/ENSG00000102218-RP2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RP2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75695
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000102218-RP2/subcellular

![](https://images.proteinatlas.org/909/2123_E6_29_blue_red_green.jpg)
![](https://images.proteinatlas.org/909/2123_E6_42_blue_red_green.jpg)
![](https://images.proteinatlas.org/909/2131_F4_16_blue_red_green.jpg)
![](https://images.proteinatlas.org/909/2131_F4_57_blue_red_green.jpg)
![](https://images.proteinatlas.org/909/2168_B9_26_blue_red_green.jpg)
![](https://images.proteinatlas.org/909/2168_B9_40_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75695-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
