---
type: protein-evaluation
gene: "STUB1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## STUB1 — REJECTED (研究热度过高 (PubMed strict=293，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | STUB1 / CHIP |
| 蛋白名称 | E3 ubiquitin-protein ligase CHIP |
| 蛋白大小 | 303 aa / 34.9 kDa |
| UniProt ID | Q9UNE7 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus; Mitochondrion |
| 蛋白大小 | 10/10 | ×1 | 10 | 303 aa / 34.9 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=293 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=89.3; PDB: 4KBQ, 6EFK, 6NSV, 7TB1, 8EHZ, 8EI0, 8F14 |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR045202, IPR041312, IPR011990, IPR019734, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **96.0/180** | |
| **归一化总分** | | | **53.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus; Mitochondrion | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- mitochondrion (GO:0005739)
- nuclear inclusion body (GO:0042405)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- protein folding chaperone complex (GO:0101031)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 293 |
| PubMed broad count | 804 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: CHIP |

**关键文献**:
1. GDF15 induces immunosuppression via CD48 on regulatory T cells in hepatocellular carcinoma.. *Journal for immunotherapy of cancer*. PMID: 34489334
2. HSP90β Impedes STUB1-Induced Ubiquitination of YTHDF2 to Drive Sorafenib Resistance in Hepatocellular Carcinoma.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 37515378
3. Autosomal dominant cerebellar ataxias: new genes and progress towards treatments.. *The Lancet. Neurology*. PMID: 37479376
4. Trehalose induces autophagy via lysosomal-mediated TFEB activation in models of motoneuron degeneration.. *Autophagy*. PMID: 30335591
5. The chaperone-assisted selective autophagy complex dynamics and dysfunctions.. *Autophagy*. PMID: 36594740

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.3 |
| 高置信度残基 (pLDDT>90) 占比 | 78.2% |
| 置信残基 (pLDDT 70-90) 占比 | 13.5% |
| 中等置信 (pLDDT 50-70) 占比 | 1.3% |
| 低置信 (pLDDT<50) 占比 | 6.9% |
| 有序区域 (pLDDT>70) 占比 | 91.7% |
| 可用 PDB 条目 | 4KBQ, 6EFK, 6NSV, 7TB1, 8EHZ, 8EI0, 8F14, 8F15, 8F16, 8F17 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（4KBQ, 6EFK, 6NSV, 7TB1, 8EHZ, 8EI0, 8F14, 8F15, 8F16, 8F17）+ AlphaFold极高置信度预测（pLDDT=89.3），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR045202, IPR041312, IPR011990, IPR019734, IPR003613; Pfam: PF12895, PF18391, PF04564 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| HSPA8 | 0.999 | 0.995 | — |
| UBE2D1 | 0.999 | 0.996 | — |
| HSP90AA1 | 0.999 | 0.983 | — |
| HSP90AB1 | 0.999 | 0.818 | — |
| HSPA4 | 0.999 | 0.995 | — |
| BAG3 | 0.999 | 0.775 | — |
| UBE2N | 0.999 | 0.989 | — |
| BAG2 | 0.997 | 0.777 | — |
| UBE2V1 | 0.996 | 0.954 | — |
| UBE2D3 | 0.996 | 0.968 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| tobi | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| inaD | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| qkr58E-3 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Hsc70-4 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Pgant6 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Cpr11A | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Hsp70Ab | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| alphaTub84B | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG4612 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| RalGPS | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.3 + PDB: 4KBQ, 6EFK, 6NSV, 7TB1, 8EHZ,  | pLDDT=89.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Mitochondrion / Nucleoplasm, Cytosol | 一致 |
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
1. STUB1 — E3 ubiquitin-protein ligase CHIP，研究基础较多，新颖性有限。
2. 蛋白大小303 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 293 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 293 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UNE7
- Protein Atlas: https://www.proteinatlas.org/ENSG00000103266-STUB1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=STUB1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UNE7
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000103266-STUB1/subcellular

![](https://images.proteinatlas.org/43531/2148_G11_56_blue_red_green.jpg)
![](https://images.proteinatlas.org/43531/2148_G11_78_blue_red_green.jpg)
![](https://images.proteinatlas.org/43531/2152_C2_22_blue_red_green.jpg)
![](https://images.proteinatlas.org/43531/2152_C2_40_blue_red_green.jpg)
![](https://images.proteinatlas.org/43531/767_D12_1_red_green.jpg)
![](https://images.proteinatlas.org/43531/767_D12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9UNE7-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
