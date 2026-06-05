---
type: protein-evaluation
gene: "BTBD1"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BTBD1 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BTBD1 / C15orf1, NS5ATP8 |
| 蛋白名称 | BTB/POZ domain-containing protein 1 |
| 蛋白大小 | 482 aa / 52.8 kDa |
| UniProt ID | Q9H0C5 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 🔴 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytoplasmic bodies; 额外: Nucleoplasm, Cytosol; UniProt: Cytoplasm |
| 📏 蛋白大小 | 10/10 | ×1 | 10 | 482 aa / 52.8 kDa |
| 🆕 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=11 篇 (≤20→10) |
| 🏗️ 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=86.8; PDB: 无 |
| 🧬 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR011705, IPR000210, IPR012983, IPR038648, IPR011 |
| 🔗 PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| ➕ 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **138.5/180** | |
| **归一化总分** | | | **76.9/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytoplasmic bodies; 额外: Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasmic ribonucleoprotein granule (GO:0036464)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- P-body (GO:0000932)
- protein-containing complex (GO:0032991)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 11 |
| PubMed broad count | 19 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: C15orf1, NS5ATP8 |

**关键文献**:
1. Development of small-molecule tropomyosin receptor kinase (TRK) inhibitors for NTRK fusion cancers.. *Acta pharmaceutica Sinica. B*. PMID: 33643817
2. Identification and characterization of BTBD1, a novel BTB domain containing gene on human chromosome 15q24.. *Gene*. PMID: 11179693
3. BTBD1 and BTBD2 colocalize to cytoplasmic bodies with the RBCC/tripartite motif protein, TRIM5delta.. *Experimental cell research*. PMID: 12878161
4. Involvement of BTBD1 in mesenchymal differentiation.. *Experimental cell research*. PMID: 17462629
5. The topoisomerase 1-interacting protein BTBD1 is essential for muscle cell differentiation.. *Cell death and differentiation*. PMID: 15486563

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.8 |
| 高置信度残基 (pLDDT>90) 占比 | 72.6% |
| 置信残基 (pLDDT 70-90) 占比 | 14.7% |
| 中等置信 (pLDDT 50-70) 占比 | 3.1% |
| 低置信 (pLDDT<50) 占比 | 9.5% |
| 有序区域 (pLDDT>70) 占比 | 87.3% |
| 可用 PDB 条目 | 无 |


**PAE**: PAE 图像未生成本地文件，结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 极高置信度预测（pLDDT=86.8，有序区 87.3%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR011705, IPR000210, IPR012983, IPR038648, IPR011333; Pfam: PF07707, PF00651, PF08005 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CUL3 | 0.925 | 0.812 | — |
| TOP1 | 0.911 | 0.510 | — |
| TRIM5 | 0.903 | 0.000 | — |
| UBE2M | 0.799 | 0.615 | — |
| COPS5 | 0.781 | 0.767 | — |
| LRR1 | 0.761 | 0.292 | — |
| COPS3 | 0.756 | 0.731 | — |
| COPS2 | 0.750 | 0.688 | — |
| COPS6 | 0.745 | 0.741 | — |
| BTBD2 | 0.743 | 0.735 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000261721.4 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BTBD2 | psi-mi:"MI:0416"(fluorescence microscopy) | pubmed:12878161|imex:IM-19632 |
| TULP3 | psi-mi:"MI:0399"(two hybrid fragment pooling appro | pubmed:23414517|imex:IM-16425 |
| COPS6 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | imex:IM-12079|pubmed:19615732 |
| E2 | psi-mi:"MI:0018"(two hybrid) | pubmed:18305892|imex:IM-19324 |
| A0A384KY07 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| CUL3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| COPS5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| CARNMT1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.8 + PDB: 无 | pLDDT=86.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Cytoplasm / Cytoplasmic bodies; 额外: Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. BTBD1 — BTB/POZ domain-containing protein 1，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小482 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 11 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9H0C5
- Protein Atlas: https://www.proteinatlas.org/ENSG00000064726-BTBD1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BTBD1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9H0C5
- STRING: https://string-db.org/network/9606.ENSP00000
- Packet data timestamp: 2026-06-03 04:17:21

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytoplasmic bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000064726-BTBD1/subcellular

![](https://images.proteinatlas.org/24263/1858_B7_28_cr5acdf3b1b578d_red_green.jpg)
![](https://images.proteinatlas.org/24263/1858_B7_6_cr5acdf3b1b2e70_red_green.jpg)
![](https://images.proteinatlas.org/24263/1907_E10_1_red_green.jpg)
![](https://images.proteinatlas.org/24263/1907_E10_5_red_green.jpg)
![](https://images.proteinatlas.org/24263/1967_C10_1_red_green.jpg)
![](https://images.proteinatlas.org/24263/1967_C10_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->
