---
type: protein-evaluation
gene: "AGFG1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, scored, nucleus-cytoplasm, full-reevaluate]
status: scored
nuclear_score: 5
---

# AGFG1 (HRB/RAB/RIP) -- Full Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| 基因名 / 别名 | AGFG1 / HRB, RAB, RIP |
| 蛋白全称 | Arf-GAP domain and FG repeat-containing protein 1 |
| UniProt ID | P52594 |
| 蛋白大小 | 562 aa / 58.3 kDa |
| 评估日期 | 2026-06-03 |
| Sheet4 来源 | Sheet4, nuclear_score=6 |
| HPA 主定位 | Vesicles (Supported reliability) |
| 分类 | nucleus-cytoplasm (UniProt 支持核定位，HPA 定位于 Vesicles) |

## 2. 核定位证据

### UniProt Subcellular Location
| 定位 | 证据等级 |
|------|----------|
| Nucleus | ECO:0000269 (experimental, x2) |
| Cytoplasmic vesicle | ECO:0000269 (experimental) |

### GO Cellular Component
| GO ID | Term | Evidence |
|-------|------|----------|
| GO:0005643 | nuclear pore | TAS:ProtInc |
| GO:0005829 | cytosol | TAS:Reactome |
| GO:0031410 | cytoplasmic vesicle | IBA:GO_Central |
| GO:0005737 | cytoplasm | IBA:GO_Central |
| GO:0043025 | neuronal cell body | IEA:Ensembl |
| GO:0042995 | cell projection | IEA:Ensembl |

### HPA Subcellular Localization
- **Main location**: Vesicles
- **Additional locations**: None
- **Reliability (IF)**: Supported
- **IF Display Images Available**: YES (6 images from 3 cell line samples)
- **Note**: HPA 未检测到 Nucleoplasm/Nucleus/Nuclear pore 定位

### IF 图像获取状态
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF display images 可用（6 张，来自 A-431, U2OS, U-251MG 细胞株）。HPA 记录显示 Vesicles 定位，无核定位条目。

### 核定位评估
AGFG1 的核定位证据同样存在 UniProt-HPA 分歧。UniProt 以实验证据 (ECO:0000269 x2) 支持 Nucleus 定位，GO-CC 以 TAS (Traceable Author Statement) 支持 nuclear pore 定位。但 HPA 免疫荧光将 AGFG1 定位于 Vesicles (Supported 可靠性)，未检出核信号。nuclear pore 的 GO 注释提示 AGFG1 可能定位于核孔复合体（核膜结构），这可能是 HPA 将其识别为 Vesicles 的原因（核周囊泡样信号）。此外，AGFG1 作为 HIV-1 Rev 蛋白的辅因子，参与 Rev-responsive element (RRE) RNA 的核输出，这一定位与 nuclear pore 功能高度吻合。**核定位特异性评分: 5/10**（UniProt 实验证据 + nuclear pore GO 支持核关联，但 HPA 定位于 Vesicles；核孔定位可能被 HPA 分类为囊泡/核周信号）。

### Sheet4 数据差异说明
原 Sheet4 记录 AGFG1 的 HPA 为 "Nucleoplasm"，nuclear_score=6。Harvest packet (2026-06-03) 中 HPA subcellular_location=["Vesicles"]。该差异可能源于：(1) HPA 数据库更新/分类调整；(2) 核孔周质信号被 HPA 图像分析归类为 Vesicles；(3) 旧版 HPA 使用了不同的分析标准。本报告以 harvest packet 数据为主，同时纳入 UniProt 实验证据。

## 3. HPA Immunofluorescence

6 张 IF display images 可用。Image status: if_display_images_available。HPA 分类为 "Supported" 可靠性。图像显示囊泡样细胞质分布模式。由于 AGFG1 含有 FG (phenylalanine-glycine) repeat 区域（核孔蛋白的标志性序列），且 GO-CC 注释为 nuclear pore，HPA 观察到的 Vesicles 信号可能实际对应于核孔复合体或核周囊泡/运输中间体。但 HPA 官方分类为 Vesicles，未标注 nuclear pore。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "AGFG1"[Title/Abstract] AND (gene OR protein OR hydrolase) | 14 | |
| Symbol-only: "AGFG1"[Title/Abstract] | 17 | |
| Broad: "AGFG1" | 306 | **High count due to AGFG1 alias collision with other terms** |
| Aliases observed | HRB, RAB, RIP (not used for scoring) | |

**Research Volume Assessment**: PubMed strict count = 14，处于极度新颖区间（≤20）。Broad count (306) 偏高，可能因别名 HRB (HIV-1 Rev-binding) 和 RAB 在文献中的广泛使用导致干扰。Strict query (含 gene/protein/hydrolase 限定) 已有效过滤大部分别名干扰。主要研究方向：(1) HIV-1 Rev 辅因子功能 -- AGFG1 结合 HIV-1 Rev 蛋白，促进 RRE-containing RNA 的核输出；(2) acrosome biogenesis -- AGFG1 参与顶体形成中的囊泡对接/融合；(3) 癌症中的表达调控。

**关键文献**:
- PMID:39089666 -- AGFG1 increases cholesterol biosynthesis to promote PDAC progression (Cancer Lett, 2024)
- PMID:29351916 -- AGFG1 genomic alterations in pulmonary carcinoid tumors (Clin Cancer Res, 2018)
- PMID:21284487 -- Organization patterns of AGFG genes: evolutionary study (2011)

**新颖性评分: 10/10**（PubMed strict=14，极度新颖）。

## 5. AlphaFold / PAE / PDB

### AlphaFold Structure
| 指标 | 数值 |
|------|------|
| Entry ID | AF-P52594-F1 (v6) |
| Mean pLDDT | 56.1 |
| pLDDT >90 | 19.8% |
| pLDDT 70-90 | 5.3% |
| pLDDT 50-70 | 15.1% |
| pLDDT <50 | **59.8%** |

结构质量差：近 60% 的残基 pLDDT<50，提示严重无序。仅 19.8% 残基 pLDDT>90。蛋白质可能含有大量 IDR（intrinsically disordered regions），尤其是 FG repeat 区域（核孔蛋白 FG repeats 典型无序）。

### Experimental PDB Structures (3 structures, all partial)
| PDB ID | Method | Resolution | Coverage | Domain |
|--------|--------|------------|----------|--------|
| 2D9L | NMR | - | A=14-134 | ArfGAP domain |
| 2OLM | X-ray | 1.48 A | A=4-141 | ArfGAP domain |
| 2VX8 | X-ray | 2.20 A | A/B/C/D=136-175 | FG repeat region (HIV-1 Rev binding peptide) |

**结构评估**: 3 个实验结构覆盖 ArfGAP domain (NMR + X-ray 1.48 A) 和 FG repeat 肽段 (X-ray 2.20 A，与 Rev 蛋白的复合结构)。ArfGAP domain 结构质量高。AlphaFold 预测中 59.8% 的无序区域主要对应 FG repeat 区域——核孔蛋白 FG repeats 天然具有高度柔性和无序性，这是其功能特征而非结构缺陷。FG repeats 的无序性使其能形成选择性通透屏障（核孔复合体的核心机制）。**三维结构评分: 3/10**（实验结构仅覆盖 30% 全长，AlphaFold 60% 无序 -- 但 FG repeat 无序性具有功能意义）。

## 6. InterPro / Pfam Domains

| 来源 | Domain ID | 描述 |
|------|-----------|------|
| InterPro | IPR001164 | ArfGAP domain |
| InterPro | IPR037278 | ArfGAP domain superfamily |
| InterPro | IPR038508 | ArfGAP domain superfamily |
| InterPro | IPR052248 | Arf-GAP domain and FG repeat-containing protein |
| Pfam | PF01412 | ArfGAP |

### FG Repeat 区域的特殊意义
AGFG1 的 FG (phenylalanine-glycine) repeat 区域是核孔蛋白 (nucleoporins) 的标志性序列。核孔复合体中的 FG-Nups 通过其柔性 FG repeats 形成选择性通透屏障，调控核质运输。AGFG1 含有此序列，强烈提示其可能作为核孔复合体的动态组分或核运输调控因子。结合其 HIV-1 Rev 辅因子功能（促进 RRE RNA 核输出），FG repeats 是其核心功能域。

**结构域评估**: AGFG1 具有双重功能域：(1) **ArfGAP domain** -- Arf GTPase 激活，调控囊泡形成和运输，与顶体 biogenesis 功能一致；(2) **FG repeats** -- 核孔蛋白特征序列，介导核质运输，与 HIV Rev 辅因子功能一致。ArfGAP domain 在 InterPro 中有 3 个独立条目确认。FG repeats 虽无专门的 InterPro 条目，但其序列特征和功能意义明确（核孔蛋白 FG repeats 的低复杂度序列通常不被传统结构域数据库收录）。**调控结构域评分: 6/10**（ArfGAP 3 源确认 + FG repeats 功能明确，涉及核质运输和囊泡运输双通路）。

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Database | Functional Context |
|---------|---------------|--------------|----------|-------------------|
| VAMP7 | **0.992** | **0.423** | 0.900 | Vesicle SNARE -- acrosome/lysosome fusion |
| EPS15 | **0.925** | **0.631** | 0.500 | Endocytosis adaptor, EGFR pathway |
| GDI2 | 0.901 | 0 | 0 | Rab GDP dissociation inhibitor |
| GDI1 | 0.858 | 0 | 0 | Rab GDP dissociation inhibitor |
| FCHO1 | 0.846 | 0.292 | 0.500 | Clathrin-mediated endocytosis |
| ITSN1 | 0.805 | 0.230 | 0.500 | Intersectin -- endocytosis scaffold |
| STON2 | 0.780 | 0 | 0.500 | Endocytosis adaptor |
| ITSN2 | 0.770 | 0 | 0.500 | Intersectin-2 |
| RAB3A | 0.768 | 0 | 0 | Rab GTPase -- exocytosis |
| VTI1B | 0.755 | 0 | 0 | v-SNARE -- Golgi/endosome fusion |
| EPS15L1 | 0.747 | 0.233 | 0.500 | EPS15-like endocytosis adaptor |
| EPN2 | 0.738 | 0 | 0.500 | Epsin-2 -- endocytosis |
| DAB2 | 0.734 | 0 | 0.500 | Disabled-2 -- clathrin adaptor |
| RAB1A | 0.732 | 0 | 0 | Rab GTPase -- ER-Golgi transport |
| VAMP2 | 0.721 | 0 | 0.500 | v-SNARE -- synaptic vesicle fusion |

### IntAct (15 Experimental Interactions)
| Partner | Method | PMID | Notes |
|---------|--------|------|-------|
| VAMP7 | two hybrid | 18775314 | STRING+IntAct 双库验证 (STRING 0.992) |
| APC | two hybrid pooling | 20936779 | Adenomatous polyposis coli |
| VCAM1 | cross-linking | 22623428 | Vascular cell adhesion molecule |
| TGOLN2 | BioID | 29568061 | TGN protein -- Golgi |
| DNAJC5 | BRET | 29997244 | CSP-alpha, synaptic chaperone |
| MFHAS1 | protein array | 29513927 | TLR signaling regulator |
| NYAP2 | two hybrid prey pooling | 25416956 | Neuronal Tyr-phosphorylated adaptor |
| ABL2 | pull down | 31585087 | Abl2 tyrosine kinase |
| AGFG2 | anti tag co-IP | 28514442 | AGFG2 -- sister ArfGAP+FG protein |
| POLE2 | two hybrid | 25416956 | DNA polymerase epsilon subunit |
| Xpo1 (mouse) | pull down | 26673895 | Exportin-1/CRM1 -- **nuclear export receptor** |
| MPP1 | anti tag co-IP | 26496610 | MAGUK p55 family -- membrane scaffold |
| CEP170 | BioID | 26638075 | Centrosomal protein |
| HDDC3 | anti tag co-IP | 33961781 | HD domain-containing |
| FCGR2A | anti tag co-IP | 33961781 | Fc gamma receptor |

### PPI 网络评估
AGFG1 的 PPI 网络质量高且功能一致。VAMP7 在 STRING (0.992, experimental=0.423) 和 IntAct (two hybrid) 双库验证 -- VAMP7 是 acrosome/溶酶体 SNARE，与 AGFG1 在顶体形成中的功能高度吻合。EPS15 在 STRING 中有高实验分 (0.631)。STRING Top 15 中多个内吞/囊泡运输相关蛋白 (EPS15, FCHO1, ITSN1, STON2, EPN2, DAB2, VAMP2)，网络功能集中于囊泡运输和内吞作用。**关键发现**: Xpo1 (Exportin-1/CRM1) 的 pull down 互作 (PMID:26673895) -- Xpo1 是经典的核输出受体，这一互作与 AGFG1 的 HIV Rev 辅因子/核输出功能直接相关。**PPI 网络评分: 8/10**（VAMP7 强实验验证 + 双库确认，EPS15 高实验分，Xpo1 核输出连接，网络功能一致）。

## 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 5/10 | ×4 | 20 | UniProt Nucleus (ECO:0000269实验); GO nuclear pore (TAS); HPA Vesicles (Supported, 未检出核信号); 核孔/Rev辅因子功能暗示核关联 |
| 蛋白大小 | 7/10 | ×1 | 7 | 562 aa / 58.3 kDa -- 生化实验理想大小 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 (≤20)，极度新颖 |
| 三维结构 | 3/10 | ×3 | 9 | AlphaFold pLDDT=56.1, 59.8%<50 (FG repeats天然无序); 3个实验PDB结构(~30%全长) |
| 调控结构域 | 6/10 | ×2 | 12 | ArfGAP (3源确认) + FG repeats (核孔蛋白标志); 核质运输+囊泡运输双功能 |
| PPI网络 | 8/10 | ×3 | 24 | VAMP7双库验证(STRING 0.992); EPS15实验分0.631; Xpo1核输出连接; 网络功能一致 |
| **加权总分** | | | **122/180** | |
| **归一化总分 (÷1.83)** | | | **66.7/100** | |

## 9. 最终决定

**SCORED: 66.7/100 -- 保留为中等优先级候选**

AGFG1 是一个研究极新的蛋白 (PubMed 14)，具有独特的 FG repeat + ArfGAP 双重功能域。PPI 网络质量高（VAMP7 双库验证，EPS15 高实验分，Xpo1 核输出连接）。但其核定位存在 UniProt-HPA 分歧：UniProt 以实验证据支持 Nucleus 定位且 GO 注释为 nuclear pore，而 HPA 将其分类为 Vesicles。AGFG1 的 FG repeats 和 HIV Rev 辅因子功能强烈提示其与核质运输的关联。

**优势**:
- 极度新颖 (PubMed=14)
- 独特的 FG repeat + ArfGAP 双重功能域
- VAMP7 强验证 PPI (STRING 0.992 experimental + IntAct Y2H)
- EPS15 高实验分 (0.631)
- Xpo1/CRM1 互作 -- 直接连接核输出通路
- HIV-1 Rev 辅因子功能 -- 已建立的核质运输功能
- 蛋白大小理想 (58.3 kDa)
- nuclear pore GO 注释 (TAS:ProtInc)

**劣势**:
- **HPA 未检出核信号** (Vesicles 分类) -- 需独立验证核定位
- AlphaFold 结构质量差 (59.8% 无序) -- 但 FG repeats 的无序性具功能意义
- 研究主要集中于 HIV/spermatogenesis，与 TE 调控的直接关联未建立
- Broad PubMed count (306) 提示别名干扰（但 strict=14 已有效过滤）

**推荐**: 保留为中等优先级候选。AGFG1 最独特的价值在于其 FG repeat + ArfGAP 组合，连接了核质运输 (FG) 和囊泡运输 (ArfGAP)。如果核孔/核定位得到独立验证，该蛋白的核质运输调控功能将成为 TE-related RNA 核输出的潜在研究方向。Xpo1 互作为此提供了直接机制连接。建议优先进行核定位验证实验。

## 10. Manual Review Note

原 Sheet4 记录 AGFG1 的 HPA 为 "Nucleoplasm"，nuclear_score=6。Harvest packet (2026-06-03) HPA 数据显示 Vesicles。但 GO-CC nuclear pore (TAS) + UniProt Nucleus (ECO:0000269) + FG repeats（核孔蛋白标志）+ HIV Rev cofactor（核输出功能）四重证据强烈提示 AGFG1 与核质运输的关联。hPAA 的 Vesicles 分类可能将核孔复合体/核周囊泡信号归类为囊泡。

该蛋白最引人注目的是 FG repeats（核孔蛋白的特征序列）与 HIV Rev 辅因子功能的共振 -- 核孔 FG-Nups 正是通过其 FG repeats 与核运输受体 (如 Xpo1/CRM1) 互作来介导核质转运。AGFG1 的 FG repeats + Xpo1 pull down 互作构成了一个完整的核输出机制图景。ArfGAP domain 可能在此过程中调控囊泡/膜的动态。

**与 TE 调控的潜在连接**: 如果 AGFG1 参与 RNA 核输出 (通过 FG repeats 和 Xpo1 互作)，则可能也参与 TE-derived RNA 的核质运输调控。这是一个值得深入探索的方向。

---

## 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P52594
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P52594
- STRING: https://string-db.org/network/9606.ENSP00000340358
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/P52594/
- Protein Atlas: https://www.proteinatlas.org/ENSG00000173744-AGFG1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGFG1[Title/Abstract]

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (supported)。来源: https://www.proteinatlas.org/ENSG00000173744-AGFG1/subcellular

![](https://images.proteinatlas.org/8741/100_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8741/100_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8741/101_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8741/101_F5_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/8741/82_F5_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/8741/82_F5_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P52594-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P52594 |
| SMART | SM00105; |
| UniProt Domain [FT] | DOMAIN 11..135; /note="Arf-GAP"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00288" |
| InterPro | IPR052248;IPR037278;IPR001164;IPR038508; |
| Pfam | PF01412; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000173744-AGFG1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| EPS15 | Intact, Biogrid | true |
| EGFR | Biogrid | false |
| FCHO1 | Biogrid | false |
| NYAP2 | Intact | false |
| OGT | Biogrid | false |
| POLE2 | Intact | false |
| RAB11A | Biogrid | false |
| VAMP7 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
