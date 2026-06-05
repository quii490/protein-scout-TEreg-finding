---
type: protein-evaluation
gene: "EAPP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## EAPP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | EAPP / C14orf11 |
| 蛋白名称 | E2F-associated phosphoprotein |
| 蛋白大小 | 285 aa / 32.8 kDa |
| UniProt ID | Q56P03 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; 额外: Nuclear speckles; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 285 aa / 32.8 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=74.7; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR019370; Pfam: PF10238 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nuclear speckles | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 129 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C14orf11 |

**关键文献**:
1. Genetic expression analysis of E2F-associated phosphoprotein in stress responses in the mouse.. *Gene*. PMID: 26802973
2. Endothelium-specific deletion of amyloid-β precursor protein exacerbates endothelial dysfunction induced by aging.. *Aging*. PMID: 34382945
3. Spatiotemporal Expression of EAPP Modulates Neuronal Apoptosis and Reactive Astrogliosis After Spinal Cord Injury.. *Journal of cellular biochemistry*. PMID: 25704466
4. EAPP: gatekeeper at the crossroad of apoptosis and p21-mediated cell-cycle arrest.. *Oncogene*. PMID: 21258403
5. Regulation of the E2F-associated phosphoprotein promoter by GC-box binding proteins.. *The international journal of biochemistry & cell biology*. PMID: 18588995

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.7 |
| 高置信度残基 (pLDDT>90) 占比 | 28.4% |
| 置信残基 (pLDDT 70-90) 占比 | 31.9% |
| 中等置信 (pLDDT 50-70) 占比 | 29.1% |
| 低置信 (pLDDT<50) 占比 | 10.5% |
| 有序区域 (pLDDT>70) 占比 | 60.3% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=74.7，有序区 60.3%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR019370; Pfam: PF10238 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PRPF8 | 0.926 | 0.836 | — |
| EFTUD2 | 0.917 | 0.832 | — |
| AAR2 | 0.916 | 0.853 | — |
| TSSC4 | 0.895 | 0.814 | — |
| SNRNP200 | 0.867 | 0.836 | — |
| CD2BP2 | 0.853 | 0.817 | — |
| DDX23 | 0.830 | 0.805 | — |
| GPATCH1 | 0.830 | 0.829 | — |
| DHX35 | 0.828 | 0.827 | — |
| ECD | 0.817 | 0.814 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| AAR2 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBE3A | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| UBQLN4 | psi-mi:"MI:0397"(two hybrid array) | pubmed:16713569|imex:IM-11827| |
| Prpf8 | psi-mi:"MI:0676"(tandem affinity purification) | imex:IM-11719|pubmed:20360068 |
| Q7CL55 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| BYSL | psi-mi:"MI:1112"(two hybrid prey pooling approach) | pubmed:32296183|imex:IM-25472 |
| TNFAIP8 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| SNRPE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SNRPN | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| DDX23 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=74.7 + PDB: 无 | pLDDT=74.7, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm; 额外: Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. EAPP — E2F-associated phosphoprotein，非常新颖，仅有少数基础研究。
2. 蛋白大小285 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q56P03
- Protein Atlas: https://www.proteinatlas.org/ENSG00000129518-EAPP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=EAPP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q56P03
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000129518-EAPP/subcellular

![](https://images.proteinatlas.org/71031/1800_E8_1_red_green.jpg)
![](https://images.proteinatlas.org/71031/1800_E8_2_red_green.jpg)
![](https://images.proteinatlas.org/71031/2082_D7_1_red_green.jpg)
![](https://images.proteinatlas.org/71031/2082_D7_2_red_green.jpg)
![](https://images.proteinatlas.org/71031/2162_H3_2_red_green.jpg)
![](https://images.proteinatlas.org/71031/2162_H3_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q56P03-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
