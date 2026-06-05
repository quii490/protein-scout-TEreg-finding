---
type: protein-evaluation
gene: "AGBL5"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, scored, nucleus-cytoplasm, full-reevaluate]
status: scored
nuclear_score: 4
---

# AGBL5 (CCP5) -- Full Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| 基因名 / 别名 | AGBL5 / CCP5 |
| 蛋白全称 | Cytosolic carboxypeptidase-like protein 5 |
| UniProt ID | Q8NDL9 |
| 蛋白大小 | 886 aa / 97.5 kDa |
| 评估日期 | 2026-06-03 |
| Sheet4 来源 | Sheet4, nuclear_score=4 |
| HPA 主定位 | Cytokinetic bridge, Primary cilium (Approved reliability) |
| 分类 | nucleus-cytoplasm (UniProt 支持核定位，HPA 未检测到核信号) |

## 2. 核定位证据

### UniProt Subcellular Location
| 定位 | 证据等级 |
|------|----------|
| Nucleus | ECO:0000269 (experimental) |
| Cytoplasm, cytosol | ECO:0000250 (sequence similarity) |
| Cytoplasm, cytoskeleton, spindle | ECO:0000269 (experimental) |
| Midbody | ECO:0000269 (experimental) |

### GO Cellular Component
| GO ID | Term | Evidence |
|-------|------|----------|
| GO:0005634 | nucleus | IDA:UniProtKB |
| GO:0005829 | cytosol | ISS:UniProtKB |
| GO:0030496 | midbody | IDA:UniProtKB |
| GO:0072686 | mitotic spindle | IDA:UniProtKB |
| GO:0005737 | cytoplasm | IDA:LIFEdb |
| GO:0015630 | microtubule cytoskeleton | IBA:GO_Central |

### HPA Subcellular Localization
- **Main locations**: Cytokinetic bridge, Primary cilium
- **Additional locations**: Microtubules, Centriolar satellite, Basal body
- **Reliability (IF)**: Approved
- **IF Display Images Available**: YES (14 images from 7 cell line samples)
- **Note**: HPA 未检测到 Nucleoplasm/Nucleus 定位

### IF 图像获取状态
HPA IF display images 可用（14 张，来自 A-431, U2OS, U-251MG 等细胞株）。图像显示微管/中心粒/纤毛/胞质分裂桥定位模式。HPA 记录中无核定位条目。

### 核定位评估
AGBL5 的核定位证据存在来源分歧。UniProt 明确列出 Nucleus (ECO:0000269 实验证据)，GO-CC 以 IDA:UniProtKB 支持 nucleus。但 HPA 免疫荧光实验未检测到核信号——HPA subcellular_location 全部为胞质/细胞骨架相关定位（Cytokinetic bridge, Primary cilium, Microtubules, Centriolar satellite, Basal body），reliability="Approved"。这种 UniProt vs HPA 的矛盾可能来自：(1) 细胞类型/条件依赖的核定位（特定条件下入核）；(2) 核定位信号较弱，HPA 抗体/染色条件下不易检出；(3) UniProt 实验条件下的特殊发现。**核定位特异性评分: 4/10**（UniProt 实验证据支持核定位，但 HPA Approved 可靠性下未检出核信号，核定位可能为条件性或弱信号）。

### Sheet4 数据差异说明
原 Sheet4 记录 HPA 为 "Nucleoplasm"，nuclear_score=4。Harvest packet (2026-06-03) 中 HPA subcellular_location 无任何核定位条目。差异可能源于 HPA 数据库更新或旧版抓取差异。本报告以 harvest packet 数据为准，同时纳入 UniProt 实验证据。

## 3. HPA Immunofluorescence

14 张 IF display images 可用。Image status: if_display_images_available。图像显示 AGBL5 在细胞质中以微管/中心粒/初级纤毛模式分布，在分裂细胞中定位于胞质分裂桥 (cytokinetic bridge) 和中体 (midbody)。HPA 分类为 "Approved" 可靠性。图像中未见明显核定位信号，与 HPA subcellular_location 记录一致（均为胞质/细胞骨架定位）。但须注意：IF 图像的解读依赖抗体特异性和染色条件，弱核信号可能在标准染色条件下不易检出。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "AGBL5"[Title/Abstract] AND (gene OR protein OR hydrolase) | 14 | |
| Symbol-only: "AGBL5"[Title/Abstract] | 21 | |
| Broad: "AGBL5" | 24 | |
| Alias observed | CCP5 (not used for scoring) | |

**Research Volume Assessment**: PubMed strict count = 14，处于极度新颖区间（≤20）。研究集中于：(1) AGBL5 在 retinitis pigmentosa (RP) 中的致病突变 -- AGBL5 是 RP 的致病基因之一 (PMID:26720455)；(2) 微管蛋白去谷氨酰化 (deglutamylation) 功能 -- AGBL5/CCP5 是 tubulin carboxypeptidase，移除 alpha/beta-tubulin C 端 polyglutamate 修饰 (PMID:39528655)；(3) CGAS 去谷氨酰化调控先天免疫 -- AGBL5 对 CGAS 的去谷氨酰化激活抗病毒防御。

**新颖性评分: 10/10**（PubMed strict=14，极度新颖）。

## 5. AlphaFold / PAE / PDB

### AlphaFold Structure
| 指标 | 数值 |
|------|------|
| Entry ID | AF-Q8NDL9-F1 (v6) |
| Mean pLDDT | 69.8 |
| pLDDT >90 | 51.0% |
| pLDDT 70-90 | 5.5% |
| pLDDT 50-70 | 2.1% |
| pLDDT <50 | **41.3%** |

结构质量中等：51% 残基 pLDDT>90（高质量折叠域），但 41.3% 残基 pLDDT<50（无序区域）。无序区域可能对应结构域间连接和未解析的插入区域。

### Experimental PDB Structures (10 structures)
| PDB ID | Method | Resolution | Coverage | Notes |
|--------|--------|------------|----------|-------|
| 8V3M | X-ray | 1.80 A | A=2-338, 425-605 | Catalytic domain |
| 8V3N | X-ray | 2.30 A | A=2-338, 425-605 | With inhibitor |
| 8V3O | X-ray | 2.30 A | A=2-338, 425-605 | With inhibitor |
| 8V3P | X-ray | 2.36 A | A=2-338, 425-605 | Catalytic domain |
| 8V3Q | EM | 3.10 A | A=2-605 | Full catalytic + N-terminal |
| 8V3R | EM | 3.40 A | A=2-605 | With bound tubulin peptide |
| 8V3S | EM | 3.60 A | A=2-605 | Complex |
| 8V4K | EM | 3.10 A | E=2-605 | Complex |
| 8V4L | EM | 2.90 A | E=2-605 | Complex |
| 8V4M | EM | 3.00 A | E=2-605 | Complex |

**结构评估**: 10 个实验结构（4 X-ray + 6 cryo-EM），涵盖催化域和全长。分辨率从 1.80 A (X-ray) 到 3.60 A (EM)。多个结构包含底物/抑制剂共晶。这是结构数据非常丰富的一个蛋白，尤其考虑到其新颖性（PubMed 14）。AlphaFold 预测中 41.3% 无序区域可能对应 N 端延伸和域间连接（实验结构中未解析的部分）。**三维结构评分: 8/10**（10 个实验结构，含底物复合体，分辨率良好）。

## 6. InterPro / Pfam Domains

| 来源 | Domain ID | 描述 |
|------|-----------|------|
| InterPro | IPR050821 | M14 metallocarboxypeptidase |
| InterPro | IPR034286 | Cytosolic carboxypeptidase-like |
| InterPro | IPR040626 | Cytosolic carboxypeptidase N-terminal domain |
| InterPro | IPR000834 | Peptidase M14, carboxypeptidase A |
| Pfam | PF18027 | Cytosolic carboxypeptidase N-terminal domain |
| Pfam | PF00246 | Peptidase M14 (Zn carboxypeptidase) |

**结构域评估**: AGBL5 属于 M14 金属羧肽酶家族，具有 deglutamylase 活性。核心功能为移除 tubulin C 端 polyglutamate 修饰（一种重要的微管蛋白翻译后修饰）。Tubulin glutamylation 调控微管稳定性、马达蛋白结合和纤毛功能。AGBL5 也参与 CGAS（cyclic GMP-AMP synthase）的去谷氨酰化，激活 cGAS-STING 先天免疫通路。M14 羧肽酶结构域在 4 个 InterPro 条目中有不同层级确认。结构域功能与微管/纤毛调控和先天免疫直接相关。**调控结构域评分: 6/10**（M14 carboxypeptidase 具有 deglutamylase 功能，调控 tubulin PTM 和 CGAS-STING 通路，但与经典染色质/TE 调控域类型不同）。

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Textmining | Functional Context |
|---------|---------------|--------------|------------|-------------------|
| TTLL6 | 0.702 | 0 | 0.702 | Tubulin tyrosine ligase-like -- tubulin glutamylase (opposing enzyme) |
| TTLL4 | 0.688 | 0 | 0.684 | Tubulin polyglutamylase |
| CGAS | 0.626 | 0 | 0.626 | cGAS-STING pathway -- AGBL5 substrate |
| TTL | 0.575 | 0 | 0.575 | Tubulin tyrosine ligase |
| TTLL5 | 0.567 | 0 | 0.567 | Tubulin polyglutamylase |
| TTLL10 | 0.544 | 0 | 0.544 | Tubulin polyglutamylase |
| TTLL1 | 0.539 | 0 | 0.505 | Tubulin polyglutamylase |
| AGBL4 | 0.518 | 0 | 0.518 | CCP6 -- sister deglutamylase |
| SPATA46 | 0.497 | 0 | 0.497 | Spermatogenesis associated |
| CLP1 | 0.477 | 0 | 0.477 | tRNA splicing/processing |
| TTLL11 | 0.474 | 0 | 0.474 | Tubulin polyglutamylase |
| OSBPL6 | 0.437 | 0 | 0.437 | Oxysterol binding |
| EVA1A | 0.437 | 0 | 0.436 | Autophagy regulator |
| TMEM214 | 0.436 | 0 | 0.220 | Transmembrane protein |
| CEP41 | 0.436 | 0 | 0.425 | Centrosomal protein, ciliopathy |

### IntAct (15 Experimental Interactions)
| Partner | Method | PMID | Notes |
|---------|--------|------|-------|
| TPCN2 | anti tag co-IP | 28514442 | Two-pore calcium channel |
| HAVCR2 | anti tag co-IP | 28514442 | TIM-3 immune checkpoint |
| IL20RA | anti tag co-IP | 28514442 | Cytokine receptor |
| GFOD1 | anti tag co-IP | 28514442 | Glucose-fructose oxidoreductase |
| RELL2 | anti tag co-IP | 28514442 | RELT-like protein |
| HSPA8 | anti tag co-IP | 33961781 | Hsc70 chaperone |
| APPBP2 | anti tag co-IP | 33961781 | APP-binding, protein transport |
| DNAJA2 | anti tag co-IP | 33961781 | Hsp40 co-chaperone |
| BTNL9 | anti tag co-IP | 33961781 | Butyrophilin-like |
| KCNE3 | anti tag co-IP | 33961781 | Potassium channel subunit |
| CAMK2A | anti tag co-IP | 33961781 | CaMKII alpha kinase |
| PRPS2 | anti tag co-IP | 33961781 | Phosphoribosyl pyrophosphate synthetase |
| PIPSL | anti tag co-IP | 33961781 | PIP5K1A pseudogene product |
| FTL | anti tag co-IP | 33961781 | Ferritin light chain |
| SLC31A1 | anti tag co-IP | 33961781 | Copper transporter CTR1 |

### PPI 网络评估
AGBL5 的 PPI 网络质量偏低。STRING 显示 TTLL 家族 tubulin glutamylase 连接（text-mining only，实验分=0），逻辑上与其 deglutamylase 功能形成对立/互补关系。CGAS (STRING 0.626) 为其已知底物。但这些连接均为 text-mining 推断，**缺乏实验验证**。IntAct 收录 15 个 co-IP 互作，均来自两篇高通量相互作用组研究 (PMID:28514442, 33961781)。互作对象功能高度分散（离子通道、免疫检查点、细胞因子受体、代谢酶等），缺乏功能一致性，提示可能为背景结合。**PPI 网络评分: 3/10**（STRIND 全部 text-mining，IntAct 为高通量 co-IP 缺乏功能富集，TTLL/CGAS 连接无实验验证）。

## 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 4/10 | ×4 | 16 | UniProt Nucleus (ECO:0000269实验证据); HPA未检出核信号(Approved可靠性, 全为胞质/细胞骨架定位); GO Nucleus (IDA) |
| 蛋白大小 | 5/10 | ×1 | 5 | 886 aa / 97.5 kDa -- 中等偏大 |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=14 (≤20)，极度新颖 |
| 三维结构 | 8/10 | ×3 | 24 | 10个实验结构(X-ray+EM), 1.80-3.60A; AlphaFold pLDDT=69.8, 51%>90 |
| 调控结构域 | 6/10 | ×2 | 12 | M14 carboxypeptidase/deglutamylase; tubulin PTM调控; CGAS-STING通路; 非经典染色质调控域 |
| PPI网络 | 3/10 | ×3 | 9 | STRING全部text-mining(实验分=0); IntAct高通量co-IP缺乏功能富集; TTLL/CGAS连接未实验验证 |
| **加权总分** | | | **116/180** | |
| **归一化总分 (÷1.83)** | | | **63.4/100** | |

## 9. 最终决定

**SCORED: 63.4/100 -- 保留观察，核定位需独立验证**

AGBL5 是一个研究极新的蛋白 (PubMed 14)，结构数据异常丰富 (10 个实验结构)，功能明确（tubulin deglutamylase）。但其核定位证据存在 UniProt-HPA 分歧：UniProt 以实验证据 (ECO:0000269) 支持 Nucleus 定位，而 HPA Approved 可靠性下未检出核信号。PPI 网络缺乏实验验证（全部 text-mining）。该蛋白的得分主要由新颖性 (10) 和结构 (8) 驱动，核定位和 PPI 为明显弱点。

**优势**:
- 极度新颖 (PubMed=14)
- 结构数据极为丰富 (10 个实验 PDB 结构，含底物复合体)
- 功能明确 -- tubulin deglutamylase，在纤毛/微管调控中有重要角色
- Retinitis pigmentosa 致病基因 -- 具有明确的疾病关联
- CGAS-STING 先天免疫通路连接

**劣势**:
- **核定位存在 UniProt-HPA 分歧** -- 需独立实验验证
- PPI 网络零实验验证 -- TTLL/CGAS 连接仅为 text-mining
- 蛋白功能与微管/纤毛调控相关，与染色质/TE 调控的直接关联不明确
- IntAct co-IP 互作功能高度分散，提示可能为背景

**推荐**: 保留观察，但需优先进行核定位的独立验证（如核质分离 Western blot 或 IF 检测不同细胞系/条件下的核定位）。如果核定位无法独立验证，应降级或拒绝。

## 10. Manual Review Note

原 Sheet4 记录 AGBL5 的 HPA 为 "Nucleoplasm"，nuclear_score=4。Harvest packet (2026-06-03) HPA 数据无任何核定位条目（全部为 Cytokinetic bridge, Primary cilium, Microtubules, Centriolar satellite, Basal body）。此差异导致核定位评分从预期值下调至 4/10。UniProt 的实验证据 (ECO:0000269 Nucleus) 是维持核定位评分>3 的唯一依据。如果 UniProt 的核定位证据在实际验证中被推翻，该蛋白将触发 nuclear≤3 拒绝。

该蛋白的结构数据 (10 PDB) 和新颖性 (PubMed 14) 非常突出。如果核定位得到独立验证，评分可能上调。但目前 HPA Approved 数据不支持核定位，建议优先进行实验验证。

---

## 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8NDL9
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8NDL9
- STRING: https://string-db.org/network/9606.ENSP00000323833
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q8NDL9/
- Protein Atlas: https://www.proteinatlas.org/ENSG00000084693-AGBL5
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGBL5[Title/Abstract]

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytokinetic bridge (approved)。来源: https://www.proteinatlas.org/ENSG00000084693-AGBL5/subcellular

![](https://images.proteinatlas.org/30981/1773_G1_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/30981/1773_G1_7_blue_red_green.jpg)
![](https://images.proteinatlas.org/30981/2124_C4_31_blue_red_green.jpg)
![](https://images.proteinatlas.org/30981/2124_C4_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/30981/2132_C9_11_blue_red_green.jpg)
![](https://images.proteinatlas.org/30981/2132_C9_30_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8NDL9-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
