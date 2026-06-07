---
type: protein-evaluation
gene: "BCL2L1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## BCL2L1 — REJECTED (研究热度过高 (PubMed strict=650，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BCL2L1 / BCL2L, BCLX |
| 蛋白名称 | Bcl-2-like protein 1 |
| 蛋白大小 | 233 aa / 26.0 kDa |
| UniProt ID | Q07817 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Mitochondria; 额外: Nucleoli fibrillar center, Acrosome; UniProt: Mitochondrion inner membrane; Mitochondrion outer membrane;  |
| 蛋白大小 | 10/10 | ×1 | 10 | 233 aa / 26.0 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=650 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=72.5; PDB: 1BXL, 1G5J, 1LXL, 1MAZ, 1R2D, 1R2E, 1R2G |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013279, IPR036834, IPR046371, IPR026298, IPR002 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Mitochondria; 额外: Nucleoli fibrillar center, Acrosome | Approved |
| UniProt | Mitochondrion inner membrane; Mitochondrion outer membrane; Mitochondrion matrix; Cytoplasmic vesicl... | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- Bcl-2 family protein complex (GO:0097136)
- centrosome (GO:0005813)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- endoplasmic reticulum (GO:0005783)
- mitochondrial inner membrane (GO:0005743)
- mitochondrial matrix (GO:0005759)
- mitochondrial outer membrane (GO:0005741)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 650 |
| PubMed broad count | 5134 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BCL2L, BCLX |

**关键文献**:
1. The landscape of somatic copy-number alteration across human cancers.. *Nature*. PMID: 20164920
2. Erythroid/megakaryocytic differentiation confers BCL-XL dependency and venetoclax resistance in acute myeloid leukemia.. *Blood*. PMID: 36508699
3. USP13 facilitates a ferroptosis-to-autophagy switch by activation of the NFE2L2/NRF2-SQSTM1/p62-KEAP1 axis dependent on the KRAS signaling pathway.. *Autophagy*. PMID: 39360581
4. Systematic RNA interference reveals that oncogenic KRAS-driven cancers require TBK1.. *Nature*. PMID: 19847166
5. The TP53 Apoptotic Network Is a Primary Mediator of Resistance to BCL2 Inhibition in AML Cells.. *Cancer discovery*. PMID: 31048320

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.5 |
| 高置信度残基 (pLDDT>90) 占比 | 38.2% |
| 置信残基 (pLDDT 70-90) 占比 | 18.5% |
| 中等置信 (pLDDT 50-70) 占比 | 12.0% |
| 低置信 (pLDDT<50) 占比 | 31.3% |
| 有序区域 (pLDDT>70) 占比 | 56.7% |
| 可用 PDB 条目 | 1BXL, 1G5J, 1LXL, 1MAZ, 1R2D, 1R2E, 1R2G, 1R2H, 1R2I, 1YSG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（1BXL, 1G5J, 1LXL, 1MAZ, 1R2D, 1R2E, 1R2G, 1R2H, 1R2I, 1YSG）+ AlphaFold极高置信度预测（pLDDT=72.5），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013279, IPR036834, IPR046371, IPR026298, IPR002475; Pfam: PF00452, PF02180 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| BID | 0.999 | 0.990 | — |
| HRK | 0.999 | 0.835 | — |
| PMAIP1 | 0.999 | 0.741 | — |
| TP53 | 0.999 | 0.986 | — |
| BECN1 | 0.999 | 0.956 | — |
| BCL2 | 0.999 | 0.863 | — |
| BIK | 0.999 | 0.873 | — |
| BAX | 0.999 | 0.999 | — |
| BBC3 | 0.999 | 0.911 | — |
| BAD | 0.999 | 0.999 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000504536.1 | psi-mi:"MI:0071"(molecular sieving) | pubmed:15131699 |
| ENSMUSP00000105445.4 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:15131699 |
| BAD | psi-mi:"MI:0018"(two hybrid) | pubmed:9388232|mint:MINT-52217 |
| BAX | psi-mi:"MI:0411"(enzyme linked immunosorbent assay | pubmed:9388232|mint:MINT-52217 |
| BAK1 | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:15901672 |
| Bcl2l11 | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:15694340 |
| BBC3 | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:15694340 |
| Bmf | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:15694340 |
| BIK | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:15694340 |
| HRK | psi-mi:"MI:0107"(surface plasmon resonance) | pubmed:15694340 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.5 + PDB: 1BXL, 1G5J, 1LXL, 1MAZ, 1R2D,  | pLDDT=72.5, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane; Mitochondrion outer  / Mitochondria; 额外: Nucleoli fibrillar center, Acros | 一致 |
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
1. BCL2L1 — Bcl-2-like protein 1，研究基础较多，新颖性有限。
2. 蛋白大小233 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 650 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 650 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q07817
- Protein Atlas: https://www.proteinatlas.org/ENSG00000171552-BCL2L1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BCL2L1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q07817
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Mitochondria (approved)。来源: https://www.proteinatlas.org/ENSG00000171552-BCL2L1/subcellular

![](https://images.proteinatlas.org/35734/2199_A9_15_blue_red_green.jpg)
![](https://images.proteinatlas.org/35734/2199_A9_44_blue_red_green.jpg)
![](https://images.proteinatlas.org/35734/859_A2_4_blue_red_green.jpg)
![](https://images.proteinatlas.org/35734/859_A2_5_blue_red_green.jpg)
![](https://images.proteinatlas.org/35734/862_A2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/35734/862_A2_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q07817-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q07817 |
| SMART | SM00337;SM00265; |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR013279;IPR036834;IPR046371;IPR026298;IPR002475;IPR004725;IPR020717;IPR020726;IPR020728;IPR003093;IPR020731; |
| Pfam | PF00452;PF02180; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000171552-BCL2L1/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BAD | Intact, Biogrid | true |
| BAK1 | Intact, Biogrid | true |
| BCL2L11 | Intact, Biogrid | true |
| BECN1 | Intact, Biogrid | true |
| BID | Intact, Biogrid | true |
| BIK | Intact, Biogrid | true |
| BMF | Intact, Biogrid | true |
| MAPK8 | Intact, Biogrid | true |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
