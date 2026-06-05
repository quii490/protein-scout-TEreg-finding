---
type: protein-evaluation
gene: "KIAA0930"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## KIAA0930 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | KIAA0930 / C22orf9 |
| 蛋白名称 | Uncharacterized protein KIAA0930 |
| 蛋白大小 | 404 aa / 45.8 kDa |
| UniProt ID | Q6ICG6 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 4/10 | ×4 | 16 | HPA: Nuclear membrane, Mitochondria; 额外: Nucleoplasm; UniProt: 无注释 |
| 蛋白大小 | 10/10 | ×1 | 10 | 404 aa / 45.8 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=4 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=72.2; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019141; Pfam: PF09741 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **121.0/180** | |
| **归一化总分** | | | **67.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear membrane, Mitochondria; 额外: Nucleoplasm | Approved |
| UniProt | 无注释 | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- 无 GO-CC 注释

**结论**: 核定位信号较弱，多个数据源显示混合定位或非核偏好。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 4 |
| PubMed broad count | 4 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C22orf9 |

**关键文献**:
1. Protein-altering germline mutations implicate novel genes related to lung cancer development.. *Nature communications*. PMID: 32393777
2. Alternative splicing analysis showed the splicing factor polypyrimidine tract-binding protein 1 as a potential target in acute myeloid leukemia therapy.. *Neoplasma*. PMID: 36131606
3. Genetics of facial telangiectasia in the Rotterdam Study: a genome-wide association study and candidate gene approach.. *Journal of the European Academy of Dermatology and Venereology : JEADV*. PMID: 33095951
4. The uncharacterized transcript KIAA0930 confers a cachexic phenotype on cancer cells.. *Oncotarget*. PMID: 37477523

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 72.2 |
| 高置信度残基 (pLDDT>90) 占比 | 41.3% |
| 置信残基 (pLDDT 70-90) 占比 | 19.1% |
| 中等置信 (pLDDT 50-70) 占比 | 9.4% |
| 低置信 (pLDDT<50) 占比 | 30.2% |
| 有序区域 (pLDDT>70) 占比 | 60.4% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=72.2，有序区 60.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019141; Pfam: PF09741 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SFN | 0.829 | 0.829 | — |
| YWHAE | 0.715 | 0.715 | — |
| YWHAG | 0.645 | 0.626 | — |
| YWHAZ | 0.637 | 0.637 | — |
| FRYL | 0.627 | 0.627 | — |
| YWHAQ | 0.624 | 0.624 | — |
| YWHAB | 0.607 | 0.598 | — |
| C11orf16 | 0.507 | 0.000 | — |
| WRN | 0.457 | 0.457 | — |
| C4orf19 | 0.447 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| YWHAQ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAG | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAZ | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| YWHAB | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| USP11 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| YWHAH | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| PEF1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ITGB3BP | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CBY1 | psi-mi:"MI:2222"(inference by socio-affinity scori | pubmed:unassigned1312 |
| FRYL | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=72.2 + PDB: 无 | pLDDT=72.2, v6 | 仅预测 |
| 定位 | UniProt + HPA | 无注释 / Nuclear membrane, Mitochondria; 额外: Nucleoplasm | 待确认 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致: +0
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. KIAA0930 — Uncharacterized protein KIAA0930，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小404 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 4 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q6ICG6
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100364-KIAA0930/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=KIAA0930
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q6ICG6
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear membrane (approved)。来源: https://www.proteinatlas.org/ENSG00000100364-KIAA0930/subcellular

![](https://images.proteinatlas.org/38091/428_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38091/428_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/38091/433_B12_2_red_green.jpg)
![](https://images.proteinatlas.org/38091/433_B12_3_red_green.jpg)
![](https://images.proteinatlas.org/38091/440_B12_1_red_green.jpg)
![](https://images.proteinatlas.org/38091/440_B12_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q6ICG6-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
