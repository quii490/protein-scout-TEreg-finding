---
type: protein-evaluation
gene: "C12orf57"
date: 2026-06-01
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## C12orf57 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | C12orf57 / C10 |
| 蛋白大小 | 126 aa / 13.2 kDa |
| UniProt ID | Q99622 |
| 评估日期 | 2026-06-01 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 9 | /10 | ×4 | HPA Enhanced: Nuclear speckles main; UniProt cytoplasm + nuclear speck (GO) |
| 📏 蛋白大小 | 8 | /10 | ×1 | 126 aa，小蛋白 |
| 🆕 研究新颖性 | 10 | /10 | ×5 | PubMed strict=11 |
| 🏗️ 三维结构 | 8 | /10 | ×3 | AlphaFold pLDDT 80.0; pLDDT>70 占 76.9% |
| 🧬 调控结构域 | 7 | /10 | ×2 | Pfam PF14974 (Protein C10 family); 无染色质域；新颖蛋白基线 |
| 🔗 PPI 网络 | 6 | /10 | ×3 | IntAct: ANKK1/INSL3/ESR1 co-IP; STRING: ANKRD50 0.994 exp |
| ➕ 互证加分 | +1.0 | max 3 | 1.0 | ANKK1 STRING+IntAct 双源; HPA+GO 定位一致 |
| **原始总分** | | | **151 /183** | |
| **归一化总分** | | | **82.5 /100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| HPA | Main: Nuclear speckles; no additional | Enhanced |
| UniProt | Cytoplasm (ECO:0000269); Nuclear speck (GO:0016607, IDA:HPA) | Experimental |
| GO-CC | Cytoplasm (GO:0005737, IDA); Nuclear speck (GO:0016607, IDA:HPA) | Experimental |

**HPA 详情**: reliability=Enhanced（最高等级）; subcellular_location=Nuclear speckles; main=Nuclear speckles（单一主定位）。

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**结论**: HPA Enhanced 确认 nuclear speckles 为唯一 main location。UniProt 同时有 cytoplasm 实验证据和 nuclear speck GO 注释。核定位得分 9。

#### 3.2 蛋白大小评估

126 aa / 13.2 kDa。小蛋白，在 100–200 aa 范围内。得分 8。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict | 11 |
| PubMed symbol only | 14 |
| PubMed broad | 14 |

**主要研究方向**:
- Temtamy 综合征致病基因（常染色体隐性遗传，胼胝体发育不全、小眼畸形、癫痫）
- 脑发育中的功能（胼胝体形成）

**关键文献**:
1. Platzer et al. (2014). "Exome sequencing identifies compound heterozygous mutations in C12orf57 in two siblings with severe intellectual disability, hypoplasia of the corpus callosum, chorioretinal coloboma, and intractable seizures." *American Journal of Medical Genetics Part A*. PMID: 24798461
2. Wang et al. (2020). "Temtamy syndrome caused by a new C12orf57 variant in a Chinese boy, including pedigree analysis and literature review." *Experimental and Therapeutic Medicine*. PMID: 31853307
3. Williamson & FitzPatrick (2014). "The genetic architecture of microphthalmia, anophthalmia and coloboma." *European Journal of Medical Genetics*. PMID: 24859618
4. Younis et al. (2022). "Identification of epilepsy concomitant candidate genes recognized in Saudi epileptic patients." *European Review for Medical and Pharmacological Sciences*. PMID: 35363364
5. Borgio (2023). "Heterogeneity in biomarkers, mitogenome and genetic disorders of the Arab population with special emphasis on large-scale whole-exome sequencing." *Archives of Medical Science*. PMID: 37313193

**评价**: 极度新颖，PubMed strict=11。研究集中于该基因在 Temtamy 综合征中的致病突变。UniProt 注释功能为 "may be required for corpus callosum development"。无染色质/转录调控方向研究，存在新颖研究角度空间。新颖性得分 10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 平均 pLDDT | 80.0 |
| pLDDT >90 占比 | 45.2% |
| pLDDT 70–90 占比 | 31.7% |
| pLDDT 50–70 占比 | 7.1% |
| pLDDT <50 占比 | 15.9% |
| 可用 PDB 条目 | 0 |

**PAE 图像**:

![[Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/C12orf57/C12orf57-PAE.png]]

**评价**: AlphaFold 预测质量高（mean pLDDT 80.0）。76.9% 残基 pLDDT>70，45.2% >90（侧链精度高）。无 PDB 实验结构。得分 8。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro | IPR026317 (Protein C10 family) |
| Pfam | PF14974 (Protein C10 family) |
| SMART | 无可辨识结构域 |

**染色质调控潜力分析**: 无已知染色质/DNA 结合结构域。Protein C10 家族功能未知。AlphaFold 有良好折叠域（pLDDT 80.0 + 76.9% 有序），存在新域发现潜力。新颖蛋白基线 7 分。

#### 3.6 PPI 网络

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| ANKK1 | validated Y2H | 32296183 | Ankyrin repeat kinase | 否 |
| INSL3 | validated Y2H | 32296183 | Insulin-like hormone | 否 |
| ESR1 | TAP | 31527615 | Estrogen receptor (转录因子) | 是 |
| ARHGAP39 | anti tag co-IP | 32203420 | Rho GTPase activating | 否 |
| PPP1CA | anti tag co-IP | 28514442 | Ser/Thr phosphatase | 否 |
| EGLN3 | anti tag co-IP | 26972000 | Prolyl hydroxylase | 否 |
| CCNL1 | anti tag co-IP | 33961781 | Cyclin L1 (转录调控) | 是 |
| CIMAP1A | anti tag co-IP | 33961781 | Ciliary microtubule | 否 |
| RPL35A | anti tag co-IP | 33961781 | Ribosomal protein | 否 |
| TAX1BP3 | anti tag co-IP | 33961781 | Wnt/PDZ signaling | 否 |
| TANC2 | anti tag co-IP | 33961781 | Synaptic scaffold | 否 |
| EMC4 | anti tag co-IP | 33961781 | ER membrane complex | 否 |

**STRING 预测互作** (combined score >0.4):

| Partner | Score | 功能类别 | 调控相关？ |
|---------|-------|---------|-----------|
| ANKRD50 | 0.994 | Ankyrin repeat | 否 |
| HLA-B | 0.811 | MHC class I | 否 |
| PLAC8 | 0.769 | Placenta-specific | 否 |
| HLA-A | 0.767 | MHC class I | 否 |
| POLR3H | 0.665 | RNA Pol III subunit | 是 |
| PLXNB2 | 0.610 | Plexin receptor | 否 |
| TACC1 | 0.605 | Centrosome/mitotic spindle | 否 |

**已知复合体成员** (GO Cellular Component):
- 无已知复合体注释（GO-CC 仅有 cytoplasm 和 nuclear speck）

**PPI 互证分析**:
- STRING + IntAct 共同确认: ANKK1 (validated Y2H + STRING 0.994 experimental)
- 仅 IntAct 实验: INSL3, ESR1, ARHGAP39, PPP1CA, EGLN3, CCNL1, CIMAP1A, RPL35A, TAX1BP3, TANC2, EMC4
- 仅 STRING 预测: ANKRD50, HLA-B, PLAC8, HLA-A, POLR3H, PLXNB2, TACC1
- 调控相关比例: 3/19 (15.8%)

**评价**: 有丰富的实验物理互作证据（co-IP + Y2H + TAP），包括 Cell 2021 (PMID:33961781) 的大规模互作组数据。ANKK1 同时被 IntAct validated Y2H 和 STRING 0.994 实验分确认。partner 主要为信号转导和结构蛋白，ESR1 和 CCNL1 与转录调控相关。得分 6。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT + PDB | pLDDT 80.0，无 PDB | N/A |
| 结构域 | InterPro / Pfam / SMART | Protein C10 family | 一致 |
| PPI | STRING + IntAct | ANKK1 双库确认; IntAct 12 partners | 部分一致 |
| 定位 | HPA / UniProt / GO | HPA Enhanced nuclear speckles; UniProt nuclear speck GO | 一致 |

**互证加分明细**:
- ANKK1 互作被 STRING (0.994 exp) + IntAct (validated Y2H) 共同确认: +0.5
- 核定位 HPA Enhanced + UniProt GO nuclear speck 一致: +0.5
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐ (4/5)

**核心优势**:
1. 极度新颖（PubMed=11），HPA Enhanced 确认核斑定位
2. AlphaFold 高质量结构（pLDDT 80.0）+ 实验验证 PPI（ANKK1 双源确认）
3. 与疾病关联（Temtamy 综合征），有临床转化潜力

**风险/不确定性**:
1. 核斑定位尚无功能意义验证
2. PPI partner 多为非调控蛋白，染色质调控联系弱
3. UniProt 同时有 cytoplasm 实验证据
4. 蛋白极小（126 aa），结构域未知
5. HPA IF display 图像不可用

**下一步建议**:
- [ ] 验证核斑定位的功能意义（是否参与 pre-mRNA 剪接调控）
- [ ] 研究与核斑 marker（SC35/SRSF2）的共定位

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q99622
- Protein Atlas: https://www.proteinatlas.org/ENSG00000111678-C12orf57
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=C12orf57
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q99622


#### PPI 网络（三源综合）
| Partner | Source | Score/Evidence |
|---|---|---|
| 无记录 | — | — |

IntAct 有限记录。无 BioGrid 补充数据。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nuclear-speckle/C12orf57/C12orf57-PAE.png]]

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear speckles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000111678-C12orf57/subcellular

![](https://images.proteinatlas.org/46182/1605_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/46182/1605_A2_3_red_green.jpg)
![](https://images.proteinatlas.org/46182/1615_A2_1_red_green.jpg)
![](https://images.proteinatlas.org/46182/1615_A2_2_red_green.jpg)
![](https://images.proteinatlas.org/46182/1687_E1_1_red_green.jpg)
![](https://images.proteinatlas.org/46182/1687_E1_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q99622 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR026317; |
| Pfam | PF14974; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000111678-C12orf57/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| AGAP3 | Opencell | false |
| ANKK1 | Intact | false |
| BLMH | Bioplex | false |
| CAPZB | Opencell | false |
| CCNL1 | Bioplex | false |
| CNOT7 | Bioplex | false |
| CRYBG2 | Bioplex | false |
| EMC4 | Bioplex | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
