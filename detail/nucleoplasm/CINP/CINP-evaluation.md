---
type: protein-evaluation
gene: "CINP"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## CINP 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CINP |
| 蛋白名称 | Cyclin-dependent kinase 2-interacting protein |
| 蛋白大小 | 212 aa / 24.3 kDa |
| UniProt ID | Q9BW66 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | x4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 212 aa / 24.3 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=42 篇 (≤60→6) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=87.7; PDB: 8CIH, 8RHN, 9LGO |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR023250 |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 3.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **125.0/180** | |
| **归一化总分** | | | **69.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- nucleus (GO:0005634)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 42 |
| PubMed broad count | 234 |
| 别名(未计入scoring) |  |

**关键文献**:
1. METTL14-mediated m6A epitranscriptomic modification contributes to chemotherapy-induced neuropathic pain by stabilizing GluN2A expression via IGF2BP2.. *The Journal of clinical investigation*. PMID: 38319733
2. The SPATA5-SPATA5L1 ATPase complex directs replisome proteostasis to ensure genome integrity.. *Cell*. PMID: 38554706
3. NT-3 contributes to chemotherapy-induced neuropathic pain through TrkC-mediated CCL2 elevation in DRG neurons.. *EMBO reports*. PMID: 38594391
4. Dual function of MrgprB2 receptor-dependent neural immune axis in chronic pain.. *Journal of advanced research*. PMID: 40024332
5. SF3B1 hotspot mutations confer sensitivity to PARP inhibition by eliciting a defective replication stress response.. *Nature genetics*. PMID: 37524790

**评价**: 较新颖，有一定研究但存在未探索领域。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 87.7 |
| 高置信度残基 (pLDDT>90) 占比 | 66.0% |
| 置信残基 (pLDDT 70-90) 占比 | 18.9% |
| 中等置信 (pLDDT 50-70) 占比 | 9.9% |
| 低置信 (pLDDT<50) 占比 | 5.2% |
| 有序区域 (pLDDT>70) 占比 | 84.9% |
| 可用 PDB 条目 | 8CIH, 8RHN, 9LGO |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（8CIH, 8RHN, 9LGO）+ AlphaFold高质量预测（pLDDT=87.7），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR023250 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| C1orf109 | 0.918 | 0.797 | — |
| SUPT16H | 0.877 | 0.822 | — |
| SPATA5 | 0.869 | 0.822 | — |
| ATRIP | 0.852 | 0.361 | — |
| SPATA5L1 | 0.844 | 0.756 | — |
| RTF1 | 0.839 | 0.810 | — |
| TNKS1BP1 | 0.807 | 0.749 | — |
| SSRP1 | 0.807 | 0.749 | — |
| LEO1 | 0.805 | 0.769 | — |
| C12orf43 | 0.774 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000453839.1 | psi-mi:"MI:0067"(light scattering) | pubmed:38554706|imex:IM-30175 |
| CLUAP1 | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| zwf | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| KIF7 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| POTEE | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AFG2A | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| SPATA5L1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| AIRIM | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| HECTD1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| BLZF1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-27438|doi:10.1038/s414 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=87.7 + PDB: 8CIH, 8RHN, 9LGO | pLDDT=87.7, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +3.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐

**核心优势**:
1. CINP -- Cyclin-dependent kinase 2-interacting protein，较新颖，有一定研究但存在未探索领域。
2. 蛋白大小212 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 42 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9BW66
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100865-CINP/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CINP
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9BW66
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9BW66-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
