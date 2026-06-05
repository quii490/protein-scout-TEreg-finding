---
type: protein-evaluation
gene: "PPIB"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PPIB — REJECTED (研究热度过高 (PubMed strict=201，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PPIB / CYPB |
| 蛋白名称 | Peptidyl-prolyl cis-trans isomerase B |
| 蛋白大小 | 216 aa / 23.7 kDa |
| UniProt ID | P23284 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Endoplasmic reticulum; 额外: Nucleoplasm; UniProt: Virion; Endoplasmic reticulum lumen; Melanosome |
| 蛋白大小 | 10/10 | ×1 | 10 | 216 aa / 23.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=201 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=91.8; PDB: 1CYN, 3ICH, 3ICI, 8K0F, 8K0I, 8K0M, 8K17 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR029000, IPR020892, IPR002130; Pfam: PF00160 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Endoplasmic reticulum; 额外: Nucleoplasm | Supported |
| UniProt | Virion; Endoplasmic reticulum lumen; Melanosome | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- endoplasmic reticulum chaperone complex (GO:0034663)
- endoplasmic reticulum lumen (GO:0005788)
- extracellular exosome (GO:0070062)
- focal adhesion (GO:0005925)
- melanosome (GO:0042470)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 201 |
| PubMed broad count | 261 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CYPB |

**关键文献**:
1. Tubular cells produce FGF2 via autophagy after acute kidney injury leading to fibroblast activation and renal fibrosis.. *Autophagy*. PMID: 35491858
2. Autophagy activates EGR1 via MAPK/ERK to induce FGF2 in renal tubular cells for fibroblast activation and fibrosis during maladaptive kidney repair.. *Autophagy*. PMID: 37978868
3. Clearance of damaged mitochondria via mitophagy is important to the protective effect of ischemic preconditioning in kidneys.. *Autophagy*. PMID: 31066324
4. The structural basis for the collagen processing by human P3H1/CRTAP/PPIB ternary complex.. *Nature communications*. PMID: 39245686
5. Hub Genes PRPF19 and PPIB: Molecular Pathways and Potential Biomarkers in COPD.. *International journal of chronic obstructive pulmonary disease*. PMID: 40524719

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 91.8 |
| 高置信度残基 (pLDDT>90) 占比 | 82.4% |
| 置信残基 (pLDDT 70-90) 占比 | 0.5% |
| 中等置信 (pLDDT 50-70) 占比 | 16.2% |
| 低置信 (pLDDT<50) 占比 | 0.9% |
| 有序区域 (pLDDT>70) 占比 | 82.9% |
| 可用 PDB 条目 | 1CYN, 3ICH, 3ICI, 8K0F, 8K0I, 8K0M, 8K17, 8KC9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1CYN, 3ICH, 3ICI, 8K0F, 8K0I, 8K0M, 8K17, 8KC9）+ AlphaFold极高置信度预测（pLDDT=91.8），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR029000, IPR020892, IPR002130; Pfam: PF00160 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| P3H1 | 0.999 | 0.091 | — |
| CRTAP | 0.999 | 0.098 | — |
| BSG | 0.996 | 0.000 | — |
| PDIA4 | 0.994 | 0.657 | — |
| HSP90B1 | 0.994 | 0.546 | — |
| CALR | 0.987 | 0.306 | — |
| CAMLG | 0.969 | 0.230 | — |
| P4HB | 0.966 | 0.471 | — |
| DNAJB11 | 0.955 | 0.305 | — |
| HSPA5 | 0.955 | 0.470 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| TRAF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| DNM2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16169070|imex:IM-16517| |
| fucK | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| ftsH | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| rhsC | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| bcsG | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:15690043|mint:MINT-5217 |
| CRTAP | psi-mi:"MI:0027"(cosedimentation) | imex:IM-11997|pubmed:17055431 |
| UBQLN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| IKBKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=91.8 + PDB: 1CYN, 3ICH, 3ICI, 8K0F, 8K0I,  | pLDDT=91.8, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Virion; Endoplasmic reticulum lumen; Melanosome / Endoplasmic reticulum; 额外: Nucleoplasm | 一致 |
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
1. PPIB — Peptidyl-prolyl cis-trans isomerase B，研究基础较多，新颖性有限。
2. 蛋白大小216 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 201 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 201 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P23284
- Protein Atlas: https://www.proteinatlas.org/ENSG00000166794-PPIB/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PPIB
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P23284
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Endoplasmic reticulum (supported)。来源: https://www.proteinatlas.org/ENSG00000166794-PPIB/subcellular

![](https://images.proteinatlas.org/12720/1752_C1_2_cr5804bfa7d57a4_blue_red_green.jpg)
![](https://images.proteinatlas.org/12720/1752_C1_8_cr5804bfb37c6f5_blue_red_green.jpg)
![](https://images.proteinatlas.org/12720/200_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12720/200_B4_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/12720/202_B4_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/12720/202_B4_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P23284-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
