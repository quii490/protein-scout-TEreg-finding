---
type: protein-evaluation
gene: "NRM"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NRM — REJECTED (研究热度过高 (PubMed strict=150，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NRM / NRM29 |
| 蛋白名称 | Nurim |
| 蛋白大小 | 262 aa / 29.4 kDa |
| UniProt ID | Q8IXM6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nuclear membrane; UniProt: Nucleus inner membrane |
| 蛋白大小 | 10/10 | ×1 | 10 | 262 aa / 29.4 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=150 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=89.1; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR033580 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **86.5/180** | |
| **归一化总分** | | | **48.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane | Enhanced |
| UniProt | Nucleus inner membrane | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- membrane (GO:0016020)
- nuclear envelope (GO:0005635)
- nuclear inner membrane (GO:0005637)
- nuclear membrane (GO:0031965)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 150 |
| PubMed broad count | 3628 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NRM29 |

**关键文献**:
1. Neural mechanism underlying acupuncture analgesia.. *Progress in neurobiology*. PMID: 18582529
2. The clinical and functional effects of TERT variants in myelodysplastic syndrome.. *Blood*. PMID: 34019641
3. Real-World Application of Recently Proposed ASTCT/CIBMTR/EBMT/APBMT Consensus Risk Stratification for Transplantation-Associated Thrombotic Microangiopathy in Children.. *Transplantation and cellular therapy*. PMID: 38936547
4. Inhibition of RIP1 improves immune reconstitution and reduces GVHD mortality while preserving graft-versus-leukemia effects.. *Science translational medicine*. PMID: 38117900
5. Novel composite health assessment risk model for older allogeneic transplant recipients: BMT-CTN 1704.. *Blood advances*. PMID: 40101246

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 89.1 |
| 高置信度残基 (pLDDT>90) 占比 | 66.0% |
| 置信残基 (pLDDT 70-90) 占比 | 26.7% |
| 中等置信 (pLDDT 50-70) 占比 | 5.3% |
| 低置信 (pLDDT<50) 占比 | 1.9% |
| 有序区域 (pLDDT>70) 占比 | 92.7% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 极高置信度预测（pLDDT=89.1，有序区 92.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR033580 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SUN2 | 0.684 | 0.336 | — |
| LBR | 0.652 | 0.000 | — |
| EMD | 0.631 | 0.000 | — |
| TRIM59 | 0.593 | 0.591 | — |
| LEMD3 | 0.576 | 0.000 | — |
| LMNB1 | 0.574 | 0.000 | — |
| LMNB2 | 0.571 | 0.000 | — |
| SUN1 | 0.569 | 0.165 | — |
| TCF19 | 0.539 | 0.000 | — |
| C6orf136 | 0.529 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Dmel\CG7173 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| nanos | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG11350 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| - | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG13840 | psi-mi:"MI:0018"(two hybrid) | pubmed:14605208|imex:IM-16524| |
| Dmel\CG5597 | psi-mi:"MI:0892"(solid phase assay) | imex:IM-20952|pubmed:23827685 |
| ZG16B | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| CRNN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| TRIM59 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |
| AQP2 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=89.1 + PDB: 无 | pLDDT=89.1, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus inner membrane / Nuclear membrane | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NRM — Nurim，研究基础较多，新颖性有限。
2. 蛋白大小262 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 150 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 150 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IXM6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000137404-NRM/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NRM
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IXM6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (enhanced)。来源: https://www.proteinatlas.org/ENSG00000137404-NRM/subcellular

![](https://images.proteinatlas.org/72545/1608_C12_1_red_green.jpg)
![](https://images.proteinatlas.org/72545/1608_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/72545/1664_C12_2_red_green.jpg)
![](https://images.proteinatlas.org/72545/1664_C12_3_red_green.jpg)
![](https://images.proteinatlas.org/73982/1609_A12_1_red_green.jpg)
![](https://images.proteinatlas.org/73982/1609_A12_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IXM6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
