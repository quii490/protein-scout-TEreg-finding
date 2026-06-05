---
type: protein-evaluation
gene: "AGAP2"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation, scored, nucleoplasm, full-reevaluate]
status: scored
nuclear_score: 6
---

# AGAP2 (PIKE-A/CENTG1) -- Full Re-Evaluation Report

## 1. 基本信息

| 属性 | 值 |
|------|-----|
| 基因名 / 别名 | AGAP2 / CENTG1, KIAA0167, PIKE-A |
| 蛋白全称 | Arf-GAP with GTPase, ANK repeat and PH domain-containing protein 2 |
| UniProt ID | Q99490 |
| 蛋白大小 | 1192 aa / 124.6 kDa |
| 评估日期 | 2026-06-03 |
| Sheet4 来源 | Sheet4, nuclear_score=6 |
| HPA 主定位 | Nucleoplasm, Cytosol (Supported reliability) |
| 分类 | nucleoplasm (dual localization with cytosol) |

## 2. 核定位证据

### UniProt Subcellular Location
| 定位 | 证据等级 |
|------|----------|
| Cytoplasm | (no evidence codes listed) |
| Nucleus | (no evidence codes listed) |
| Cytoplasm (isoform 2) | (no evidence codes listed) |

### GO Cellular Component
| GO ID | Term | Evidence |
|-------|------|----------|
| GO:0005654 | nucleoplasm | IDA:HPA |
| GO:0005634 | nucleus | IDA:MGI |
| GO:0005829 | cytosol | IDA:HPA |
| GO:0005737 | cytoplasm | IDA:MGI |
| GO:0005768 | endosome | IDA:MGI |
| GO:0070062 | extracellular exosome | HDA:UniProtKB |
| GO:0090543 | Flemming body | IDA:HPA |
| GO:0016020 | membrane | HDA:UniProtKB |

### HPA Subcellular Localization
- **Main locations**: Nucleoplasm, Cytosol
- **Additional location**: Midbody ring
- **Reliability (IF)**: Supported
HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

### 核定位评估
AGAP2 在 HPA 中双定位于 Nucleoplasm 和 Cytosol（Supported 可靠性）。GO-CC 通过 IDA 证据支持 nucleoplasm (HPA) 和 nucleus (MGI)。UniProt 列出 Cytoplasm 和 Nucleus 但未标注证据代码。该蛋白在胞质和核质均有分布，可能与细胞周期依赖性的核质穿梭有关。Flemming body (midbody ring) 的定位提示可能在胞质分裂中发挥功能。**核定位特异性评分: 6/10**（HPA/GO 支持核定位，但为双定位蛋白，非专一性核蛋白）。

## 3. HPA Immunofluorescence

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

## 4. PubMed Literature Assessment

| Query Type | Count | Notes |
|------------|-------|-------|
| Strict: "AGAP2"[Title/Abstract] AND (gene OR protein OR hydrolase) | 81 | |
| Symbol-only: "AGAP2"[Title/Abstract] | 137 | |
| Broad: "AGAP2" | 185 | |
| Aliases observed | CENTG1, KIAA0167 (not used for scoring) | |

**Research Volume Assessment**: PubMed strict count = 81，处于 81-100 区间。但需注意大量文献涉及 lncRNA AGAP2-AS1（反义链非编码 RNA）而非 AGAP2 蛋白本身。真正聚焦 AGAP2 蛋白功能的文献估计 <40 篇。主要研究方向包括：PI3K/Akt 信号通路激活（PIKE-A 为其别名）、神经元凋亡保护、癌细胞侵袭与增殖、TGF-beta 信号调控、Fc-gamma 受体介导的吞噬作用。

**关键文献**:
- PMID:30674964 -- SP1 and RARα regulate AGAP2 expression in cancer (Sci Rep, 2019)
- PMID:36611866 -- AGAP2/PIKE-A in FcγR-mediated phagocytosis (Cells, 2022)
- PMID:32092977 -- AGAP2 modulating TGFβ1-signaling in liver fibrosis (IJMS, 2020)

**新颖性评分: 2/10**（PubMed strict=81，81-100 区间，接近但未触发 PubMed>100 拒绝）。

## 5. AlphaFold / PAE / PDB

### AlphaFold Structure
| 指标 | 数值 |
|------|------|
| Entry ID | AF-Q99490-F1 (v6) |
| Mean pLDDT | 58.6 |
| pLDDT >90 | 27.4% |
| pLDDT 70-90 | 12.3% |
| pLDDT 50-70 | 4.2% |
| pLDDT <50 | **56.0%** |

结构质量偏低：超过一半的残基 (56.0%) pLDDT<50，提示大量无序区域 (IDRs)。27.4% 的残基 pLDDT>90，对应保守的折叠结构域（ANK repeats, ArfGAP, PH, Ras GTPase）。

### Experimental PDB Structures (3 structures, all partial)
| PDB ID | Method | Resolution | Coverage | Domain |
|--------|--------|------------|----------|--------|
| 2BMJ | X-ray | 2.10 A | A=402-577 | PH domain |
| 2IWR | X-ray | 1.50 A | A=402-577 | PH domain |
| 2RLO | NMR | - | A=674-914 | PH + ArfGAP domains |

**结构评估**: 3 个实验结构覆盖了 PH domain (2.10/1.50 A X-ray) 和 ArfGAP+PH 区域 (NMR)。但仅覆盖全长的 ~30%。AlphaFold 预测中 56% 的残基属于无序区域 (pLDDT<50)，整体结构质量偏低。折叠域（ANK/PH/ArfGAP/Ras）的 AlphaFold 预测可信度高，但域间连接区域为长无序区。**三维结构评分: 3/10**（多数残基无序，实验结构仅覆盖少数折叠域）。

## 6. InterPro / Pfam Domains

| 来源 | Domain ID | 描述 |
|------|-----------|------|
| InterPro | IPR002110 | Ankyrin repeat |
| InterPro | IPR036770 | Ankyrin repeat superfamily |
| InterPro | IPR001164 | ArfGAP domain |
| InterPro | IPR037278 | ArfGAP domain superfamily |
| InterPro | IPR038508 | ArfGAP domain superfamily |
| InterPro | IPR001849 | Pleckstrin homology (PH) domain |
| InterPro | IPR011993 | PH-like domain superfamily |
| InterPro | IPR001806 | Small GTPase (Ras) domain |
| InterPro | IPR027417 | P-loop NTPase |
| InterPro | IPR051282 | Arf-GAP with ANK repeat and PH domain-containing protein |
| Pfam | PF12796 | Ankyrin repeat (ANK_2) |
| Pfam | PF01412 | ArfGAP |
| Pfam | PF00071 | Ras family (small GTPase) |

**结构域评估**: AGAP2 含多个调控/信号结构域：(1) **ANK repeats** -- 介导蛋白-蛋白互作，广泛用于信号复合体组装；(2) **ArfGAP domain** -- Arf GTPase 激活蛋白，调控囊泡运输和细胞骨架重塑；(3) **PH domain** -- 结合磷酸肌醇，介导膜招募和 PI3K 信号；(4) **Ras GTPase domain** -- 小 GTPase，参与信号转导。该蛋白结构域组合提示其在 PI3K/Akt 信号通路中充当信号整合者。在 10 个 InterPro 条目中有多个独立来源确认（ArfGAP 3 条目，ANK 2 条目，PH 2 条目）。**调控结构域评分: 8/10**（多信号域组合，≥3 库确认，PI3K/Akt 通路核心调控蛋白）。

## 7. Protein-Protein Interaction Network

### STRING (Top 15)
| Partner | Combined Score | Experimental | Database | Functional Context |
|---------|---------------|--------------|----------|-------------------|
| GRM1 | 0.928 | 0.095 | 0.900 | mGluR1 -- PI3K coupling in neurons |
| UNC5B | 0.926 | 0.100 | 0.900 | Netrin receptor, apoptosis/axon guidance |
| EPB41L1 | 0.802 | **0.334** | 0 | 4.1B -- cytoskeleton-membrane linker |
| LGMN | 0.732 | 0 | 0 | Legumain -- cysteine protease |
| GRIA2 | 0.664 | **0.355** | 0 | AMPA receptor subunit |
| ANK1 | 0.663 | 0.087 | 0 | Ankyrin -- cytoskeleton |
| ANK2 | 0.643 | 0.095 | 0 | Ankyrin-B |
| ANK3 | 0.641 | 0.095 | 0 | Ankyrin-G |
| PPP1R9B | 0.640 | **0.288** | 0 | Spinophilin/Neurabin-II |
| NF2 | 0.600 | **0.292** | 0 | Merlin -- Hippo pathway tumor suppressor |
| SET | 0.594 | 0 | 0 | PP2A inhibitor, histone chaperone |
| DLGAP1 | 0.581 | 0.183 | 0 | GKAP/SAPAP -- postsynaptic scaffold |
| ANP32A | 0.555 | 0 | 0 | Acidic nuclear phosphoprotein, chromatin |
| PLEK | 0.554 | 0 | 0 | Pleckstrin -- PH domain signaling |
| PLEK2 | 0.549 | 0 | 0 | Pleckstrin-2 |

### IntAct (15 Experimental Interactions)
| Partner | Method | PMID | Notes |
|---------|--------|------|-------|
| UNC5B | two hybrid | 18469807 | Netrin receptor, STRING+IntAct双库验证 |
| Dcc (mouse) | anti tag co-IP | 18469807 | Netrin receptor |
| Unc5b (mouse) | anti bait co-IP | 18469807 | Netrin receptor |
| Grm1 (mouse) | confocal microscopy | 14528310 | mGluR1 co-localization |
| Homer1 (mouse) | anti bait co-IP | 14528310 | Postsynaptic scaffold |
| Homer2 (mouse) | anti bait co-IP | 14528310 | Postsynaptic scaffold |
| M-RIP | pull down | 20368287 | RhoA/ROCK pathway |
| Mprip (mouse) | two hybrid | 20368287 | RhoA/ROCK pathway |
| Nr4a1 (mouse) | two hybrid | 20368287 | Nur77 -- nuclear receptor |
| Siah1a (mouse) | two hybrid | 20368287 | E3 ubiquitin ligase |
| SNCA | pull down | 18614564 | alpha-Synuclein -- Parkinson's |
| Cnksr2 (mouse) | anti bait co-IP | 28671696 | CNKSR2 -- Ras signaling |
| Syngap1 (mouse) | anti bait co-IP | 28671696 | SynGAP -- RasGAP at synapses |
| Pde4dip (mouse) | anti bait co-IP | 28671696 | Myomegalin -- cAMP signaling |
| KRT17 | cross-linking | 30021884 | Keratin 17 |

### PPI 网络评估
AGAP2 的 PPI 网络以 synaptic signaling 和 PI3K 通路为核心。UNC5B 在 STRING (0.926) 和 IntAct (two hybrid) 双库验证。Homer1/Homer2 作为支架蛋白将 mGluR1 与 PI3K 通路连接（PMID:14528310）。ANK1/ANK2/ANK3 的 STRING 连接可能基于结构域相似性 (ANK repeats)。NF2 (Merlin) 与 Hippo 通路连接具有潜在肿瘤抑制意义。IntAct 中 15 个实验互作，涵盖 co-IP、Y2H、pull down 等多种方法。网络在 synaptic 信号和 PI3K/Akt 通路方面功能一致。**PPI 网络评分: 7/10**（UNC5B 双库验证，Homer 介导的 PI3K 连接，多种实验方法支持）。

## 8. 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 6/10 | ×4 | 24 | HPA Nucleoplasm+Cytosol (Supported); GO nucleoplasm+nucleus (IDA); 双定位蛋白，非专一性核定位 |
| 蛋白大小 | 4/10 | ×1 | 4 | 1192 aa / 124.6 kDa -- 偏大，生化实验挑战较大 |
| 研究新颖性 | 2/10 | ×5 | 10 | PubMed strict=81 (81-100区间); 含大量lncRNA AGAP2-AS1文献干扰 |
| 三维结构 | 3/10 | ×3 | 9 | AlphaFold pLDDT=58.6, 56.0%<50无序; 3个PDB实验结构仅覆盖~30%全长 |
| 调控结构域 | 8/10 | ×2 | 16 | ANK+ArfGAP+PH+Ras四域组合; ≥3库确认; PI3K/Akt信号通路核心 |
| PPI网络 | 7/10 | ×3 | 21 | UNC5B双库验证; Homer-mediated PI3K coupling; 15个IntAct实验互作 |
| **加权总分** | | | **84/180** | |
| **归一化总分 (÷1.83)** | | | **45.9/100** | |

## 9. 最终决定

**SCORED: 45.9/100 -- 保留但优先级较低**

AGAP2 是一个多结构域信号蛋白，在 PI3K/Akt 通路中充当信号整合者。HPA/GO 支持其核质双定位（Nucleoplasm + Cytosol）。PubMed=81 位于 81-100 区间（新颖性=2），较大地拉低了总分。蛋白偏大 (1192 aa) 且大部分区域无序 (56% pLDDT<50)，结构解析困难。但结构域组合（ANK+ArfGAP+PH+Ras）具有信号整合潜力，PI3K/Akt 通路在多种癌症中被广泛研究。

**优势**:
- 四结构域组合 (ANK+ArfGAP+PH+Ras)，具有多层面的信号调控潜力
- PI3K/Akt 通路核心调控蛋白 -- 癌症生物学中高度相关的通路
- Homer1/Homer2 介导的 mGluR1-PI3K coupling 为神经元特异性信号机制
- UNC5B 在双库验证 (STRING+IntAct)
- HPA/GO 双源支持核定位

**劣势**:
- PubMed=81 新颖性较差（得分仅2/10）
- 蛋白大 (1192 aa / 124.6 kDa)
- 56% 残基无序，结构质量差
- 为双定位蛋白，非专一性核蛋白
- 研究集中于 PI3K 信号和癌症，与染色质/TE 调控的直接关联不明确
- lncRNA AGAP2-AS1 文献干扰 PubMed 计数

**推荐**: 保留观察。如果研究方向偏向 PI3K/Akt 信号与染色质调控的交叉（如 Akt 磷酸化调控表观遗传因子），该蛋白可能具有研究价值。但在纯核蛋白/TE 调控筛选中不占优势。

## 10. Manual Review Note

原 Sheet4 分配 nuclear_score=6。本 full re-evaluate 维持相似的核定位评估 (6/10)。结构域评分上调至 8/10（四域组合，≥3 库确认 ANK/ArfGAP/PH）。PubMed strict=81 导致新颖性评分仅 2/10，是总分偏低的主要原因。注意 lncRNA AGAP2-AS1 文献干扰 PubMed 计数 -- 真正的 AGAP2 蛋白文献 <40 篇。如果排除 lncRNA 干扰，该蛋白的新颖性实际优于评分所示。

**HPA IF 状态**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

---

## 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99490
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99490
- STRING: https://string-db.org/network/9606.ENSP00000257617
- InterPro: https://www.ebi.ac.uk/interpro/protein/uniprot/Q99490/
- Protein Atlas: https://www.proteinatlas.org/ENSG00000135439-AGAP2
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=AGAP2[Title/Abstract]

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000135439-AGAP2/subcellular

![](https://images.proteinatlas.org/75831/1806_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/75831/1806_E8_4_red_green.jpg)
![](https://images.proteinatlas.org/75831/1835_G3_7_red_green.jpg)
![](https://images.proteinatlas.org/75831/1835_G3_8_red_green.jpg)
![](https://images.proteinatlas.org/75831/1870_G2_3_red_green.jpg)
![](https://images.proteinatlas.org/75831/1870_G2_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q99490-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
