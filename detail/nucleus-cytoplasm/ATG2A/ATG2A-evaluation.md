---
type: protein-evaluation
gene: "ATG2A"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## ATG2A 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | ATG2A / KIAA0404 |
| 蛋白名称 | Autophagy-related protein 2 homolog A |
| 蛋白大小 | 1938 aa / 212.9 kDa |
| UniProt ID | Q2TAZ0 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:25:45 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | x4 | 16 | HPA: Vesicles; UniProt: Preautophagos... |
| 蛋白大小 | 4/10 | x1 | 4 | 1938 aa / 212.9 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=67 篇 (61-80->4) |
| 三维结构 | 7/10 | x3 | 21 | AlphaFold v6 pLDDT=67.4; PDB: 6KLR, 8KBX, ... |
| 调控结构域 | 5/10 | x2 | 10 | InterPro: 1; Pfam: 1; IPR026849 |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **103.5/180** | |
| **归一化总分 (/1.83)** | | | **56.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles; 额外: Nucleoplasm, Vesicles | Uncertain |
| UniProt | Preautophagosomal structure membrane, Lipid droplet, Endoplasmic reticulum membrane | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- endoplasmic reticulum membrane (GO:0005789)
- lipid droplet (GO:0005811)
- organelle membrane contact site (GO:0044232)
- phagophore (GO:0061908)
- phagophore assembly site (GO:0000407)
- phagophore assembly site membrane (GO:0034045)

**结论**: 核定位证据一般，存在混合定位或不一致信号，需进一步实验验证。

#### 3.2 蛋白大小评估

**评价**: 1938 aa，蛋白偏大（> 1200 aa），表达纯化难度增加，但结构域丰富。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 67 |
| PubMed broad count | 99 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: KIAA0404 |

**关键文献**:
1. Loss of WIPI4 in neurodegeneration causes autophagy-independent ferroptosis.. *Nature cell biology*. PMID: 38454050
2. Therapeutic targeting of the USP2-E2F4 axis inhibits autophagic machinery essential for zinc homeostasis in cancer progression.. *Autophagy*. PMID: 35253629
3. S-palmitoylation modulates ATG2-dependent non-vesicular lipid transport during starvation-induced autophagy.. *The EMBO journal*. PMID: 40128367
4. HIF-1α-induced expression of m6A reader YTHDF1 drives hypoxia-induced autophagy and malignancy of hepatocellular carcinoma by promoting ATG2A and ATG14 translation.. *Signal transduction and targeted therapy*. PMID: 33619246
5. ATG2A acts as a tether to regulate autophagosome-lysosome fusion in neural cells.. *Autophagy*. PMID: 40083067

**评价**: 研究较多，新颖性一般（PubMed 61-80篇）。新颖性评分 4/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.4 |
| 高置信度残基 (pLDDT>90) 占比 | 16.6% |
| 置信残基 (pLDDT 70-90) 占比 | 39.1% |
| 中等置信 (pLDDT 50-70) 占比 | 18.2% |
| 低置信 (pLDDT<50) 占比 | 26.1% |
| 有序区域 (pLDDT>70) 占比 | 55.7% |
| 可用 PDB 条目 | 6KLR, 8KBX, 8KBY, 8KC3, 8SBK, 8SBL, 8Y1L |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold中等质量预测（pLDDT=67.4），存在部分低置信区域。三维结构评分 7/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR026849; Pfam: PF13329 |

**染色质调控潜力分析**: 存在 2 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| GABARAPL1 | 0.847 | 0.193 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| EBI-2963271 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| ENSP00000366475.3 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| dinG | two hybrid pooling approach | imex:IM-13779|pubmed:20711500 |
| WIPI1 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| WDR45 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| FLNA | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| TRMT61A | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| SMN1 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| DNAJB1 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| PHB2 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.4 + PDB: 6KLR, 8KBX, 8KBY | pLDDT=67.4, v6 | 预测+实验 |
| 定位 | HPA | Nucleoplasm | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 56.6/100

**核心优势**:
1. 已有PDB实验结构：6KLR, 8KBX, 8KBY。
2. 存在 2 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 核定位信号较弱或存在矛盾（评分 4/10），需IF实验验证
2. 蛋白偏大（1938 aa），表达纯化难度大

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q2TAZ0
- Protein Atlas: https://www.proteinatlas.org/search/ATG2A
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=ATG2A
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q2TAZ0
- STRING: https://string-db.org/network/9606.ATG2A
- Packet data timestamp: 2026-06-03 03:25:45

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (uncertain)。来源: https://www.proteinatlas.org/ENSG00000110046-ATG2A/subcellular

![](https://images.proteinatlas.org/38715/435_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/38715/435_A9_5_red_green.jpg)
![](https://images.proteinatlas.org/38715/445_A9_3_red_green.jpg)
![](https://images.proteinatlas.org/38715/445_A9_5_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q2TAZ0-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q2TAZ0 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 14..111; /note="Chorein N-terminal"; /evidence="ECO:0000255" |
| InterPro | IPR026849; |
| Pfam | PF13329; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000110046-ATG2A/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| WDR45 | Intact, Biogrid | true |
| ATG9A | Intact | false |
| GABARAP | Intact | false |
| GABARAPL1 | Intact | false |
| GABARAPL2 | Intact | false |
| MAP1LC3B | Intact | false |
| TOMM40 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
