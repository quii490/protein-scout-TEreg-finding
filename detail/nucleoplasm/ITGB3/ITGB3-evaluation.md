---
type: protein-evaluation
gene: "ITGB3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## ITGB3 — REJECTED (研究热度过高 (PubMed strict=606，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ITGB3 / GP3A |
| 蛋白名称 | Integrin beta-3 |
| 蛋白大小 | 788 aa / 87.1 kDa |
| UniProt ID | P05106 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Plasma membrane; 额外: Nucleoplasm; UniProt: Cell membrane; Cell projection, lamellipodium membrane; Cell |
| 蛋白大小 | 10/10 | ×1 | 10 | 788 aa / 87.1 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=606 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=87.0; PDB: 1JV2, 1KUP, 1KUZ, 1L5G, 1M1X, 1M8O, 1MIZ |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR013111, IPR040622, IPR057073, IPR033760, IPR015 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Plasma membrane; 额外: Nucleoplasm | Supported |
| UniProt | Cell membrane; Cell projection, lamellipodium membrane; Cell junction, focal adhesion; Postsynaptic ... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- alpha9-beta1 integrin-ADAM8 complex (GO:0071133)
- alphav-beta3 integrin-HMGB1 complex (GO:0035868)
- alphav-beta3 integrin-IGF-1-IGF1R complex (GO:0035867)
- alphav-beta3 integrin-PKCalpha complex (GO:0035866)
- alphav-beta3 integrin-vitronectin complex (GO:0071062)
- apical plasma membrane (GO:0016324)
- cell surface (GO:0009986)
- cell-cell junction (GO:0005911)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 606 |
| PubMed broad count | 1550 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: GP3A |

**关键文献**:
1. Qihuang Zhuyu formula alleviates coronary microthrombosis by inhibiting PI3K/Akt/αIIbβ3-mediated platelet activation.. *Phytomedicine : international journal of phytotherapy and phytopharmacology*. PMID: 38295661
2. SLC44A2 regulates vascular smooth muscle cell phenotypic switching and aortic aneurysm.. *The Journal of clinical investigation*. PMID: 38916960
3. Cellular senescence promotes macrophage-to-myofibroblast transition in chronic ischemic renal disease.. *Cell death & disease*. PMID: 40348745
4. EDIL3/Del-1 prevents aortic dissection through enhancing internalization and degradation of apoptotic vascular smooth muscle cells.. *Autophagy*. PMID: 38873925
5. Gene Expression Linked to Reepithelialization of Human Skin Wounds.. *International journal of molecular sciences*. PMID: 36555389

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.0 |
| 高置信度残基 (pLDDT>90) 占比 | 59.4% |
| 置信残基 (pLDDT 70-90) 占比 | 30.1% |
| 中等置信 (pLDDT 50-70) 占比 | 6.3% |
| 低置信 (pLDDT<50) 占比 | 4.2% |
| 有序区域 (pLDDT>70) 占比 | 89.5% |
| 可用 PDB 条目 | 1JV2, 1KUP, 1KUZ, 1L5G, 1M1X, 1M8O, 1MIZ, 1MK7, 1MK9, 1S4X |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1JV2, 1KUP, 1KUZ, 1L5G, 1M1X, 1M8O, 1MIZ, 1MK7, 1MK9, 1S4X）+ AlphaFold极高置信度预测（pLDDT=87.0），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013111, IPR040622, IPR057073, IPR033760, IPR015812; Pfam: PF07974, PF23105, PF18372 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| ITGAV | 0.999 | 0.989 | — |
| VTN | 0.999 | 0.000 | — |
| ITGA5 | 0.999 | 0.659 | — |
| ITGA2B | 0.999 | 0.991 | — |
| TLN1 | 0.999 | 0.809 | — |
| FN1 | 0.999 | 0.977 | — |
| VWF | 0.998 | 0.236 | — |
| SRC | 0.998 | 0.309 | — |
| TLN2 | 0.996 | 0.104 | — |
| GNA13 | 0.994 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000452786.2 | psi-mi:"MI:0404"(comigration in non denaturing gel | pubmed:11606749 |
| ITGA2B | psi-mi:"MI:0369"(lex-a dimerization assay) | pubmed:14681217 |
| EBI-981051 | psi-mi:"MI:0405"(competition binding) | imex:IM-14442|pubmed:16275649 |
| ITGAV | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:11884718 |
| TLN1 | psi-mi:"MI:0114"(x-ray crystallography) | pubmed:12535520 |
| VTN | psi-mi:"MI:0892"(solid phase assay) | pubmed:1694173|imex:IM-19205 |
| FN1 | psi-mi:"MI:0892"(solid phase assay) | pubmed:1694173|imex:IM-19205 |
| VWF | psi-mi:"MI:0892"(solid phase assay) | pubmed:1694173|imex:IM-19205 |
| EBI-2855532 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CX3CL1 | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:23125415|imex:IM-26217 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.0 + PDB: 1JV2, 1KUP, 1KUZ, 1L5G, 1M1X,  | pLDDT=87.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cell membrane; Cell projection, lamellipodium memb / Plasma membrane; 额外: Nucleoplasm | 一致 |
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
1. ITGB3 — Integrin beta-3，研究基础较多，新颖性有限。
2. 蛋白大小788 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 606 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 606 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P05106
- Protein Atlas: https://www.proteinatlas.org/ENSG00000259207-ITGB3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ITGB3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P05106
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Plasma membrane (supported)。来源: https://www.proteinatlas.org/ENSG00000259207-ITGB3/subcellular

![](https://images.proteinatlas.org/27852/281_B9_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27852/281_B9_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P05106-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P05106 |
| SMART | SM00187;SM01241;SM01242;SM00423; |
| UniProt Domain [FT] | DOMAIN 30..76; /note="PSI"; /evidence="ECO:0000255"; DOMAIN 135..377; /note="VWFA"; /evidence="ECO:0000269\|PubMed:15378069, ECO:0000269\|PubMed:19111664"; DOMAIN 463..498; /note="I-EGF 1"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01392, ECO:0000269\|PubMed:19111664"; DOMAIN 499..548; /note="I-EGF 2"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01392, ECO:0000269\|PubMed:19111664"; DOMAIN 549..585; /note="I-EGF 3"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01392, ECO:0000269\|PubMed:19111664"; DOMAIN 586..625; /note="I-EGF 4"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01392, ECO:0000269\|PubMed:19111664" |
| InterPro | IPR013111;IPR040622;IPR057073;IPR033760;IPR015812;IPR014836;IPR012896;IPR036349;IPR002369;IPR032695;IPR057243;IPR016201;IPR036465; |
| Pfam | PF07974;PF23105;PF18372;PF08725;PF07965;PF00362;PF17205; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000259207-ITGB3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| ITGA2B | Intact, Biogrid | true |
| ITGAV | Intact, Biogrid | true |
| TLN1 | Intact, Biogrid | true |
| APP | Biogrid | false |
| CX3CL1 | Intact | false |
| FERMT3 | Biogrid | false |
| FGG | Intact | false |
| FLNA | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
