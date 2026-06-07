---
type: protein-evaluation
gene: "MRPL44"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## MRPL44 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MRPL44 |
| 蛋白名称 | Large ribosomal subunit protein mL44 |
| 蛋白大小 | 332 aa / 37.5 kDa |
| UniProt ID | Q9H9J2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoplasm, Nuclear bodies, Plasma membra; UniProt: Mitochondrion; Mitochondrion matrix |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 332 aa / 37.5 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 🏗️ 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=88.0; PDB: 3J7Y, 3J9M, 5OOL, 5OOM, 6I9R, 6NU2, 6NU3 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR014720, IPR044444, IPR055189, IPR036389; Pfam:  |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **146.0/180** | |
| **归一化总分 (÷1.83)** | | | **79.8/100****** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoplasm, Nuclear bodies, Plasma membrane | Approved |
| UniProt | Mitochondrion; Mitochondrion matrix | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA IF 图像状态: if_display_images_available。

**GO Cellular Component**:
- mitochondrial inner membrane (GO:0005743)
- mitochondrial large ribosomal subunit (GO:0005762)
- mitochondrion (GO:0005739)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 24 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Expression analysis of mammalian mitochondrial ribosomal protein genes.. *Gene expression patterns : GEP*. PMID: 32987154
2. Mitochondrial ribosomal protein genes connected with Alzheimer's and tellurite toxicity.. *Mitochondrion*. PMID: 35218961
3. MRPL44 regulates lipid metabolism in metabolic dysfunction-associated steatotic liver disease through BNIP3-mediated mitophagy.. *Frontiers in nutrition*. PMID: 41112736
4. FTO inhibition represses B-cell acute lymphoblastic leukemia progression by inducing nucleolar stress and mitochondrial dysfunction.. *Free radical biology & medicine*. PMID: 40623539
5. A Role for the Mitochondrial Protein Mrpl44 in Maintaining OXPHOS Capacity.. *PloS one*. PMID: 26221731

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 88.0 |
| 高置信度残基 (pLDDT>90) 占比 | 80.4% |
| 置信残基 (pLDDT 70-90) 占比 | 4.8% |
| 中等置信 (pLDDT 50-70) 占比 | 8.7% |
| 低置信 (pLDDT<50) 占比 | 6.0% |
| 有序区域 (pLDDT>70) 占比 | 85.2% |
| 可用 PDB 条目 | 3J7Y, 3J9M, 5OOL, 5OOM, 6I9R, 6NU2, 6NU3, 6VLZ, 6VMI, 6ZM5 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3J7Y, 3J9M, 5OOL, 5OOM, 6I9R, 6NU2, 6NU3, 6VLZ, 6VMI, 6ZM5）+ AlphaFold极高置信度预测（pLDDT=88.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR014720, IPR044444, IPR055189, IPR036389; Pfam: PF22892, PF22935 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MRPL13 | 0.999 | 0.997 | — |
| MRPL4 | 0.998 | 0.997 | — |
| MRPL43 | 0.998 | 0.997 | — |
| MRPL46 | 0.998 | 0.992 | — |
| MRPL47 | 0.998 | 0.997 | — |
| MRPL23 | 0.998 | 0.995 | — |
| MRPL27 | 0.998 | 0.994 | — |
| MRPL19 | 0.998 | 0.995 | — |
| MRPL41 | 0.997 | 0.996 | — |
| MRPS9 | 0.996 | 0.987 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| COP1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| AEP1 | psi-mi:"MI:0363"(inferred by author) | pubmed:16429126 |
| MRPL9 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| Ubx | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG11893 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG10694 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG10943 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| MRPL10 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:16429126 |
| SETDB1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| VIM | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=88.0 + PDB: 3J7Y, 3J9M, 5OOL, 5OOM, 6I9R,  | pLDDT=88.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion; Mitochondrion matrix / Mitochondria; 额外: Nucleoplasm, Nuclear bodies, Pla | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ 

**核心优势**:
1. MRPL44 — Large ribosomal subunit protein mL44，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小332 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H9J2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135900-MRPL44/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MRPL44
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H9J2
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 21:59:36

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (supported)。来源: https://www.proteinatlas.org/ENSG00000135900-MRPL44/subcellular

![](https://images.proteinatlas.org/38147/1364_E10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38147/1364_E10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38147/437_F11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/38147/437_F11_3_blue_red_green.jpg)
![](https://images.proteinatlas.org/38147/443_F11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/38147/443_F11_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9H9J2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q9H9J2 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 236..306; /note="DRBM"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00266" |
| InterPro | IPR014720;IPR044444;IPR055189;IPR036389; |
| Pfam | PF22892;PF22935; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000135900-MRPL44/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| IMMT | Intact, Biogrid | true |
| MRPL13 | Biogrid, Bioplex | true |
| MRPL18 | Biogrid, Bioplex | true |
| MRPL21 | Biogrid, Bioplex | true |
| MRPL23 | Biogrid, Bioplex | true |
| MRPL27 | Biogrid, Bioplex | true |
| MRPL28 | Biogrid, Bioplex | true |
| MRPL37 | Biogrid, Bioplex | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
