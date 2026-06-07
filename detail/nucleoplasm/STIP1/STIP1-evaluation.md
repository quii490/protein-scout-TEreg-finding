---
type: protein-evaluation
gene: "STIP1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STIP1 — REJECTED (研究热度过高 (PubMed strict=223，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STIP1 |
| 蛋白名称 | Stress-induced-phosphoprotein 1 |
| 蛋白大小 | 543 aa / 62.6 kDa |
| UniProt ID | P31948 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane, Cytosol; 额外: Nucleoplasm; UniProt: Cytoplasm; Nucleus; Dynein axonemal particle |
| 蛋白大小 | 10/10 | ×1 | 10 | 543 aa / 62.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=223 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.8; PDB: 1ELR, 1ELW, 2LNI, 2NC9, 3ESK, 3FWV, 7KW7 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR041243, IPR006636, IPR011990, IPR013105, IPR019 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane, Cytosol; 额外: Nucleoplasm | Approved |
| UniProt | Cytoplasm; Nucleus; Dynein axonemal particle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytosol (GO:0005829)
- dynein axonemal particle (GO:0120293)
- Golgi apparatus (GO:0005794)
- nucleus (GO:0005634)
- protein folding chaperone complex (GO:0101031)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 223 |
| PubMed broad count | 361 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Phosphorylated SHMT2 Regulates Oncogenesis Through m(6)A Modification in Lung Adenocarcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 38460155
2. Trehalose induces autophagy via lysosomal-mediated TFEB activation in models of motoneuron degeneration.. *Autophagy*. PMID: 30335591
3. The chaperone-assisted selective autophagy complex dynamics and dysfunctions.. *Autophagy*. PMID: 36594740
4. HSP90β Impedes STUB1-Induced Ubiquitination of YTHDF2 to Drive Sorafenib Resistance in Hepatocellular Carcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37515378
5. Xbp1s-FoxO1 axis governs lipid accumulation and contractile performance in heart failure with preserved ejection fraction.. *Nature communications*. PMID: 33727534

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.8 |
| 高置信度残基 (pLDDT>90) 占比 | 72.4% |
| 置信残基 (pLDDT 70-90) 占比 | 20.1% |
| 中等置信 (pLDDT 50-70) 占比 | 2.6% |
| 低置信 (pLDDT<50) 占比 | 5.0% |
| 有序区域 (pLDDT>70) 占比 | 92.5% |
| 可用 PDB 条目 | 1ELR, 1ELW, 2LNI, 2NC9, 3ESK, 3FWV, 7KW7 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1ELR, 1ELW, 2LNI, 2NC9, 3ESK, 3FWV, 7KW7）+ AlphaFold极高置信度预测（pLDDT=89.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR041243, IPR006636, IPR011990, IPR013105, IPR019734; Pfam: PF17830, PF13414, PF13424 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.999 | 0.990 | — |
| HSP90AA1 | 0.999 | 0.981 | — |
| HSPA4 | 0.999 | 0.843 | — |
| HSP90AB1 | 0.999 | 0.958 | — |
| AHSA1 | 0.998 | 0.259 | — |
| PRNP | 0.997 | 0.353 | — |
| DNAJB1 | 0.997 | 0.286 | — |
| PTGES3 | 0.996 | 0.569 | — |
| HSPA1L | 0.995 | 0.973 | — |
| CDC37 | 0.995 | 0.480 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Hsp83 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG9117 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Aldh-III | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Fas2 | psi-mi:"MI:0963"(interactome parallel affinity cap | pubmed:21447707|imex:IM-17304 |
| Lst8 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-15821|pubmed:22068330 |
| PpD3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Spn | psi-mi:"MI:0096"(pull down) | imex:IM-16527|pubmed:25294943 |
| pbl | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| anon-WO0153538.36 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-16527|pubmed:25294943 |
| Nup133 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:15710747|imex:IM-16519| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.8 + PDB: 1ELR, 1ELW, 2LNI, 2NC9, 3ESK,  | pLDDT=89.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Dynein axonemal particle / Plasma membrane, Cytosol; 额外: Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. STIP1 — Stress-induced-phosphoprotein 1，研究基础较多，新颖性有限。
2. 蛋白大小543 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 223 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 223 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P31948
- Protein Atlas: https://www.proteinatlas.org/ENSG00000168439-STIP1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STIP1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P31948
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000168439-STIP1/subcellular

![](https://images.proteinatlas.org/39291/683_F8_1_red_green.jpg)
![](https://images.proteinatlas.org/39291/683_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/39291/824_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/39291/824_F2_2_red_green.jpg)
![](https://images.proteinatlas.org/39291/884_F2_1_red_green.jpg)
![](https://images.proteinatlas.org/39291/884_F2_4_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P31948-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P31948 |
| SMART | SM00727;SM00028; |
| UniProt Domain [FT] | DOMAIN 130..169; /note="STI1 1"; DOMAIN 492..531; /note="STI1 2" |
| InterPro | IPR041243;IPR006636;IPR011990;IPR013105;IPR019734; |
| Pfam | PF17830;PF13414;PF13424;PF07719;PF13181; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000168439-STIP1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| CCDC117 | Intact, Biogrid, Opencell, Bioplex | true |
| CDC37L1 | Intact, Biogrid | true |
| DNAJB6 | Biogrid, Opencell | true |
| DNAJC7 | Biogrid, Opencell | true |
| FKBP5 | Intact, Biogrid, Opencell | true |
| FKBP8 | Biogrid, Opencell | true |
| HSP90AA1 | Intact, Biogrid, Opencell | true |
| HSP90AB1 | Intact, Biogrid, Opencell | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
