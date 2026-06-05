---
type: protein-evaluation
gene: "DYRK2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DYRK2 — REJECTED (研究热度过高 (PubMed strict=134，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DYRK2 |
| 蛋白名称 | Dual specificity tyrosine-phosphorylation-regulated kinase 2 |
| 蛋白大小 | 601 aa / 66.7 kDa |
| UniProt ID | Q92630 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 601 aa / 66.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=134 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=75.6; PDB: 3K2L, 3KVW, 4AZF, 5LXC, 5LXD, 5ZTN, 6HDP |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR042521, IPR011009, IPR000719, IPR017441, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **94.0/180** | |
| **归一化总分** | | | **52.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytoskeleton (GO:0005856)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 134 |
| PubMed broad count | 224 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Emerging roles of DYRK2 in cancer.. *The Journal of biological chemistry*. PMID: 33376136
2. Dyrk2 gene transfer suppresses hepatocarcinogenesis by promoting the degradation of Myc and Hras.. *JHEP reports : innovation in hepatology*. PMID: 37333975
3. A novel feedback loop between DYRK2 and USP28 regulates cancer homeostasis and DNA damage signaling.. *Cell death and differentiation*. PMID: 40858801
4. CAKUT variants in PRPF8, DYRK2, and CEP78: implications for splicing and ciliogenesis.. *bioRxiv : the preprint server for biology*. PMID: 40777246
5. Multiple functions of DYRK2 in cancer and tissue development.. *FEBS letters*. PMID: 31505048

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 75.6 |
| 高置信度残基 (pLDDT>90) 占比 | 62.7% |
| 置信残基 (pLDDT 70-90) 占比 | 1.7% |
| 中等置信 (pLDDT 50-70) 占比 | 1.5% |
| 低置信 (pLDDT<50) 占比 | 34.1% |
| 有序区域 (pLDDT>70) 占比 | 64.4% |
| 可用 PDB 条目 | 3K2L, 3KVW, 4AZF, 5LXC, 5LXD, 5ZTN, 6HDP, 6HDR, 6K0J, 7AKF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3K2L, 3KVW, 4AZF, 5LXC, 5LXD, 5ZTN, 6HDP, 6HDR, 6K0J, 7AKF）+ AlphaFold极高置信度预测（pLDDT=75.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR042521, IPR011009, IPR000719, IPR017441, IPR008271; Pfam: PF00069 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| DCAF1 | 0.941 | 0.778 | — |
| DDB1 | 0.911 | 0.605 | — |
| UBR5 | 0.889 | 0.625 | — |
| TP53 | 0.870 | 0.244 | — |
| ATM | 0.869 | 0.292 | — |
| DCAF7 | 0.809 | 0.599 | — |
| MDM2 | 0.703 | 0.292 | — |
| GSK3B | 0.672 | 0.331 | — |
| CEP78 | 0.640 | 0.510 | — |
| TP53AIP1 | 0.622 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| RAD54B | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| DYRK4 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| RB1CC1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| TTN | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:23602568|imex:IM-17935 |
| SAV1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| AKAP12 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| STK4 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KIF3C | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| KIF3B | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=75.6 + PDB: 3K2L, 3KVW, 4AZF, 5LXC, 5LXD,  | pLDDT=75.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Cytosol | 一致 |
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
1. DYRK2 — Dual specificity tyrosine-phosphorylation-regulated kinase 2，研究基础较多，新颖性有限。
2. 蛋白大小601 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 134 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 134 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q92630
- Protein Atlas: https://www.proteinatlas.org/ENSG00000127334-DYRK2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DYRK2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q92630
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/rejected/DYRK2/IF_images/DYRK2_IF_red_green.jpg]]



<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000127334-DYRK2/subcellular

![](https://images.proteinatlas.org/27230/249_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/27230/249_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/27230/251_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/27230/251_G6_2_red_green.jpg)
![](https://images.proteinatlas.org/27230/290_G6_1_red_green.jpg)
![](https://images.proteinatlas.org/27230/290_G6_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q92630-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
