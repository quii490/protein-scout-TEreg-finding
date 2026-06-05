---
type: protein-evaluation
gene: "DAB2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DAB2 — REJECTED (研究热度过高 (PubMed strict=418，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DAB2 / DOC2 |
| 蛋白名称 | Disabled homolog 2 |
| 蛋白大小 | 770 aa / 82.4 kDa |
| UniProt ID | P98082 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Vesicles, Plasma membrane; 额外: Nucleoli fibrillar center; UniProt: Cytoplasm; Cytoplasmic vesicle, clathrin-coated vesicle memb |
| 蛋白大小 | 10/10 | ×1 | 10 | 770 aa / 82.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=418 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=53.7; PDB: 2LSW, 6O5O, 6OVF |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR048559, IPR048561, IPR011993, IPR006020; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Vesicles, Plasma membrane; 额外: Nucleoli fibrillar center | Enhanced |
| UniProt | Cytoplasm; Cytoplasmic vesicle, clathrin-coated vesicle membrane; Membrane, clathrin-coated pit | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- clathrin-coated pit (GO:0005905)
- clathrin-coated vesicle (GO:0030136)
- clathrin-coated vesicle membrane (GO:0030665)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- fibrillar center (GO:0001650)
- focal adhesion (GO:0005925)
- lysosomal membrane (GO:0005765)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 418 |
| PubMed broad count | 582 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DOC2 |

**关键文献**:
1. TRIM16 Mediates K63-Linked Ubiquitination of DAB2 to Facilitate Vascular Calcification.. *Circulation research*. PMID: 40575853
2. Signals for sorting of transmembrane proteins to endosomes and lysosomes.. *Annual review of biochemistry*. PMID: 12651740
3. USP1 deubiquitinates Akt to inhibit PI3K-Akt-FoxO signaling in muscle during prolonged starvation.. *EMBO reports*. PMID: 32133736
4. Increased LCN2 (lipocalin 2) in the RPE decreases autophagy and activates inflammasome-ferroptosis processes in a mouse model of dry AMD.. *Autophagy*. PMID: 35473441
5. DAB2IP in cancer.. *Oncotarget*. PMID: 26658103

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 53.7 |
| 高置信度残基 (pLDDT>90) 占比 | 18.1% |
| 置信残基 (pLDDT 70-90) 占比 | 1.9% |
| 中等置信 (pLDDT 50-70) 占比 | 15.2% |
| 低置信 (pLDDT<50) 占比 | 64.8% |
| 有序区域 (pLDDT>70) 占比 | 20.0% |
| 可用 PDB 条目 | 2LSW, 6O5O, 6OVF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=53.7），有序残基占 20.0%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR048559, IPR048561, IPR011993, IPR006020; Pfam: PF21792, PF00640 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| LRP2 | 0.993 | 0.274 | — |
| DAB2IP | 0.992 | 0.294 | — |
| MYO6 | 0.986 | 0.887 | — |
| FCHO2 | 0.968 | 0.829 | — |
| GRB2 | 0.948 | 0.650 | — |
| LDLR | 0.934 | 0.333 | — |
| DVL3 | 0.910 | 0.301 | — |
| AP2B1 | 0.894 | 0.378 | — |
| TGFBR1 | 0.892 | 0.396 | — |
| AXIN1 | 0.886 | 0.345 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CFTR | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | imex:IM-12000|pubmed:17110338 |
| CDC16 | psi-mi:"MI:0018"(two hybrid) | imex:IM-15364|pubmed:21988832 |
| NCK1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| FYN | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| GRB2 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| PIK3R1 | psi-mi:"MI:0081"(peptide array) | imex:IM-11903|pubmed:17474147| |
| EBI-2843956 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| EBI-28967074 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| FN1 | psi-mi:"MI:0030"(cross-linking study) | imex:IM-14135|pubmed:19738201 |
| TGOLN2 | psi-mi:"MI:1314"(proximity-dependent biotin identi | pubmed:29568061|imex:IM-26301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=53.7 + PDB: 2LSW, 6O5O, 6OVF | pLDDT=53.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Cytoplasmic vesicle, clathrin-coated ve / Vesicles, Plasma membrane; 额外: Nucleoli fibrillar  | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. DAB2 — Disabled homolog 2，研究基础较多，新颖性有限。
2. 蛋白大小770 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 418 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=53.7），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 418 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P98082
- Protein Atlas: https://www.proteinatlas.org/ENSG00000153071-DAB2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DAB2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P98082
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Vesicles (enhanced)。来源: https://www.proteinatlas.org/ENSG00000153071-DAB2/subcellular

![](https://images.proteinatlas.org/28888/1026_C10_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28888/1026_C10_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28888/783_H11_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/28888/783_H11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/28888/785_H11_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/28888/785_H11_7_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P98082-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
