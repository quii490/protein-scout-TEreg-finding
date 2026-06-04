---
type: protein-evaluation
gene: "BCLAF1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
rejection_reason: "PubMed strict count 114 > 100 — research novelty threshold exceeded"
---

## BCLAF1 核蛋白评估（淘汰）

### 基本信息

| 属性 | 值 |
|------|-----|
| 基因名 | BCLAF1 (BTF, KIAA0164) |
| UniProt Accession | Q9NYF8 |
| 蛋白全称 | Bcl-2-associated transcription factor 1 |
| 氨基酸长度 | 920 aa |
| 分子量 | 106.1 kDa |
| 功能摘要 | Death-promoting transcriptional repressor; involved in cyclin-D1/CCND1 mRNA stability through the SNARP complex which associates with both the 3' end of the CCND1 gene and its mRNA |

### 淘汰判定

| 淘汰规则 | 阈值 | 实际值 | 触发 |
|----------|------|--------|------|
| PubMed strict count > 100 | ≤100 | 114 | **是** |
| 核定位特异性 ≤ 3 | ≥4 | 7 | 否 |

**结论**: PubMed strict count = 114，超过100篇门槛，触发了研究新颖性一票否决。该蛋白已被广泛研究，不适合作为TE调控相关蛋白的研究目标。

---

### 多维度评分

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|------|------|------|------|------|
| 核定位特异性 | 7/10 | ×4 | 28 | UniProt Nucleus/Nucleus speckle/Nucleoplasm (ECO:0000269) + GO-CC nucleoplasm IDA:UniProtKB + nuclear speck IDA:HPA + nucleus IDA:MGI。HPA检索页无可用的subcellular IF原图。 |
| 蛋白大小 | 2/10 | ×1 | 2 | 920 aa, 106.1 kDa。大型蛋白，AlphaFold预测77.0%残基pLDDT<50，高度无序，不利于结构研究。 |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=114 (query: "BCLAF1"[Title/Abstract] AND gene/protein/hydrolase)，broad=180。远超100篇上限，触发淘汰。 |
| 三维结构 | 2/10 | ×3 | 6 | PDB仅有7RJN(1.95A)和7RJR(1.45A)中330-339十肽片段，非全长结构。AlphaFold mean pLDDT=46.7，pct_gt_90仅1.4%，预测置信度极低。 |
| 调控结构域 | 2/10 | ×2 | 4 | InterPro IPR029199 (THRAP3/BCLAF1 family)、Pfam PF15440 (BCLAF1 protein family)。仅有家族水平注释，无明确功能结构域（如DNA结合域、酶活域）。 |
| PPI网络 | 4/10 | ×3 | 12 | STRING核心互作：THRAP3(0.993)、EMD(0.971)、BCL2(0.945)、CCNB1(0.940)、PNN(0.874)、SNIP1(0.869)、EIF4A3(0.810)、CLK2(0.801)。IntAct实验验证：THRAP3(CoIP)、EMD(Y2H)、GRB2(pull-down)、YWHAG(CoIP)、CSNK2A1(激酶实验)。互作网络以RNA加工和凋亡调控为主。 |
| **加权总分** | | | **52/180** | |
| **归一化总分 (÷1.8)** | | | **28.9/100** | |

---

### 核定位详细分析

**UniProt 亚细胞定位**:
- Cytoplasm
- Nucleus
- Nucleus speckle (ECO:0000269 — experimental evidence from PubMed)
- Nucleus, nucleoplasm (ECO:0000269 — experimental evidence from PubMed)

**GO-CC 细胞组分**:
- GO:0005737 cytoplasm (IEA:UniProtKB-SubCell)
- GO:0016592 mediator complex (IBA:GO_Central)
- GO:0016607 nuclear speck (IDA:HPA)
- GO:0005654 nucleoplasm (IDA:UniProtKB)
- GO:0005634 nucleus (IDA:MGI)

**HPA 免疫荧光（HPA IF）**:
HPA IF 图像已本地嵌入。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/BCLAF1/IF_images/BCLAF1_U2OS_1.jpg]]
![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/BCLAF1/IF_images/BCLAF1_U2OS_2.jpg]]

虽有实验证据支持核定位（nuclear speck + nucleoplasm 均为 ECO:0000269），且GO-CC中有IDA级别的实验证据，但由于HPA未能提供可验证的IF原图，核定位特异性得分为7而非更高。

---

### 三维结构分析

**AlphaFold 预测**:
- Entry: AF-Q9NYF8-F1 (version 6)
- Mean pLDDT: 46.7
- pLDDT >90: 1.4%
- pLDDT 70-90: 5.5%
- pLDDT 50-70: 16.1%
- pLDDT <50: 77.0%

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/BCLAF1/BCLAF1-PAE.png]]77%残基pLDDT<50表明该蛋白大部分区域为固有无序（intrinsically disordered），仅有少量有序结构域。这与920 aa的大尺寸相符合，暗示BCLAF1可能通过液-液相分离方式发挥功能。

**实验结构**:
- 7RJN: X-ray, 1.95 A, chains C/D=330-339（仅十肽，来自复合物中的短肽段）
- 7RJR: X-ray, 1.45 A, chain B=330-339（同上肽段）

两条PDB条目仅覆盖十肽片段(330-339 SRSRSRSRDR)，全长920 aa中几乎无实验结构信息。该短肽为富含丝氨酸-精氨酸的RS重复区，可能参与RNA结合或蛋白-蛋白相互作用。

---

### 调控结构域分析

| 数据库 | 条目 | 名称 |
|--------|------|------|
| InterPro | IPR029199 | THRAP3/BCLAF1 family |
| Pfam | PF15440 | BCLAF1 protein family |

结构域注释极为有限，仅在家族水平有分类。未发现明确的DNA结合结构域、酶催化结构域或其他功能结构域。BCLAF1被定义为转录抑制因子，但已知的分子机制主要通过蛋白-蛋白相互作用介导（与BCL2家族、THRAP3、SNIP1等），而非直接结合DNA。其富含RS二肽的区域可能介导与剪接体组分的相互作用，与其核speck定位一致。

---

### PPI 网络分析

**STRING 数据库 Top 15 互作伴侣**:

| 伴侣基因 | 综合得分 | 实验得分 | 数据库得分 | 文本挖掘 |
|----------|----------|----------|------------|----------|
| THRAP3 | 0.993 | 0.814 | 0.54 | 0.877 |
| EMD | 0.971 | 0.287 | 0 | 0.961 |
| BCL2 | 0.945 | 0.292 | 0 | 0.925 |
| CCNB1 | 0.940 | 0.335 | 0 | 0.912 |
| H2AX | 0.924 | 0.057 | 0 | 0.923 |
| PNN | 0.874 | 0.696 | 0 | 0.474 |
| SNIP1 | 0.869 | 0.682 | 0 | 0.589 |
| SNW1 | 0.823 | 0.359 | 0 | 0.694 |
| EIF4A3 | 0.810 | 0.613 | 0.36 | 0.192 |
| CLK2 | 0.801 | 0.781 | 0 | 0.127 |
| U2SURP | 0.797 | 0 | 0 | 0 |
| MAGOH | 0.792 | 0.591 | 0.36 | 0.147 |
| BRCA1 | 0.790 | 0 | 0 | 0.790 |
| VIRMA | 0.775 | 0.197 | 0 | 0.715 |
| ATRX | 0.769 | 0.071 | 0 | 0.218 |

**IntAct 实验互作（已验证）**:

| 互作伴侣 | 方法 | PMID |
|----------|------|------|
| THRAP3 | anti-tag coimmunoprecipitation | 26496610 |
| EMD | two hybrid | 15009215 |
| GRB2 | pull down | 12577067 |
| YWHAG | anti-bait coimmunoprecipitation | 17353931 |
| RNPS1 | anti-bait coimmunoprecipitation | 17353931 |
| CSNK2A1 | protein kinase assay (phosphorylation) | 22113938 |
| ARRB1 | anti-tag coimmunoprecipitation | 17620599 |
| ARRB2 | anti-tag coimmunoprecipitation | 17620599 |
| ESR1 | cosedimentation through density gradient | 21182205 |

PPI网络以mRNA剪接/加工因子（THRAP3、EIF4A3、MAGOH、PNN、CLK2）和凋亡调控因子（BCL2、EMD）为核心。与CCNB1和H2AX的关联暗示可能参与细胞周期调控和DNA损伤应答。

---

### 关键文献

1. **PMID: 40220379** — Zhou X et al. (2025) "Bclaf1 mediates super-enhancer-driven activation of POLR2A to enhance chromatin accessibility in nitrosamine-induced esophageal carcinogenesis." *Journal of Hazardous Materials*. 发现BCLAF1通过超级增强子激活POLR2A调控染色质可及性。

2. **PMID: 38937794** — Lee SC et al. (2024) "Macrophages as determinants and regulators of systemic sclerosis-related interstitial lung disease." *Journal of Translational Medicine*. 关联BCLAF1与巨噬细胞功能。

3. **PMID: 38636894** — Zhang P et al. (2024) "BCLAF1 drives esophageal squamous cell carcinoma progression through regulation of YTHDF2-dependent SIX1 mRNA degradation." *Cancer Letters*. 揭示BCLAF1通过m6A阅读器YTHDF2调控SIX1 mRNA稳定性。

4. **PMID: 38340178** — Yu Z et al. (2024) "BCLAF1 binds SPOP to stabilize PD-L1 and promotes the development and immune escape of hepatocellular carcinoma." *Cellular and Molecular Life Sciences*. BCLAF1通过SPOP-PD-L1轴促进肝癌免疫逃逸。

5. **PMID: 38805063** — Chen J et al. (2024) "CircZFR promotes colorectal cancer progression via stabilizing BCLAF1 and regulating the miR-3127-5p/RTKN2 axis." *Science China Life Sciences*. 环状RNA CircZFR稳定BCLAF1促进结直肠癌进展。

---

### HPA IF 图像

HPA检索页无可用的subcellular IF原图。已验证的IF图像来自本地存档（U2OS细胞系）：



---

### 最终决定

**REJECTED** — PubMed strict count = 114，超过100篇研究新颖性上限。该基因已有大量文献积累（162篇含基因名Title/Abstract，180篇全字段检索），包括多条独立的肿瘤学信号通路研究（食管癌、肝癌、结直肠癌）。不符合低研究热度的目标蛋白筛选标准。

---

### 人工审核备注

- BCLAF1为Bcl-2家族相关转录因子，位于染色体6q23.3
- 核定位证据充分但蛋白高度无序（77%残基无序），结构研究困难
- 虽功能多样（凋亡调控、RNA加工、DNA损伤应答、染色质重塑），研究过于成熟
- HPA无可靠subcellular IF原图可验证
- 自上次thin-reject后重新评估：harvest数据完整，但因PubMed>100仍不符合筛选标准
