---
type: protein-evaluation
gene: "NFATC3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NFATC3 — REJECTED (研究热度过高 (PubMed strict=261，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NFATC3 / NFAT4 |
| 蛋白名称 | Nuclear factor of activated T-cells, cytoplasmic 3 |
| 蛋白大小 | 1075 aa / 115.6 kDa |
| UniProt ID | Q12968 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Cytosol; UniProt: Cytoplasm; Nucleus |
| 蛋白大小 | 8/10 | ×1 | 8 | 1075 aa / 115.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=261 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=54.3; PDB: 2XRW, 2XS0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **78.5/180** | |
| **归一化总分** | | | **43.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Cytosol | Supported |
| UniProt | Cytoplasm; Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小基本合适，可用于常规实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 261 |
| PubMed broad count | 503 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NFAT4 |

**关键文献**:
1. A fibroblast-dependent TGF-β1/sFRP2 noncanonical Wnt signaling axis promotes epithelial metaplasia in idiopathic pulmonary fibrosis.. *The Journal of clinical investigation*. PMID: 38980870
2. Spatial Transcriptomics and Proteomics Profiling After Ischemic Stroke Reperfusion: Insights Into Vascular Alterations.. *Stroke*. PMID: 40052263
3. Cytoplasmic and nuclear NFATc3 cooperatively contributes to vascular smooth muscle cell dysfunction and drives aortic aneurysm and dissection.. *Acta pharmaceutica Sinica. B*. PMID: 40698138
4. Hepatic NFAT signaling regulates the expression of inflammatory cytokines in cholestasis.. *Journal of hepatology*. PMID: 33039404
5. NFATc3 Promotes Pulmonary Inflammation and Fibrosis by Regulating Production of CCL2 and CXCL2 in Macrophages.. *Aging and disease*. PMID: 37523510

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 54.3 |
| 高置信度残基 (pLDDT>90) 占比 | 20.9% |
| 置信残基 (pLDDT 70-90) 占比 | 7.0% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 66.6% |
| 有序区域 (pLDDT>70) 占比 | 27.9% |
| 可用 PDB 条目 | 2XRW, 2XS0 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=54.3），有序残基占 27.9%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR013783, IPR014756, IPR002909, IPR008366, IPR008967; Pfam: PF16179, PF00554 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| MAPK8 | 0.995 | 0.935 | — |
| PPP3R1 | 0.987 | 0.000 | — |
| PPP3CB | 0.956 | 0.000 | — |
| MAPK9 | 0.952 | 0.384 | — |
| PPP3CA | 0.946 | 0.000 | — |
| GATA4 | 0.940 | 0.051 | — |
| PPP3CC | 0.932 | 0.000 | — |
| MEF2A | 0.931 | 0.000 | — |
| SRF | 0.930 | 0.000 | — |
| GSK3B | 0.930 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| CDK6 | psi-mi:"MI:0424"(protein kinase assay) | pubmed:22094256|imex:IM-16628 |
| Mycbp2 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:28671696|doi:10.1038/nn |
| SUFU | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| ENSP00000300659.5 | psi-mi:"MI:0402"(chromatin immunoprecipitation ass | pubmed:20177053|imex:IM-26516 |
| EGLN3 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:26972000|imex:IM-22750 |
| CEP128 | psi-mi:"MI:1314"(proximity-dependent biotin identi | imex:IM-24512|pubmed:26638075 |
| XCL2 | psi-mi:"MI:0432"(one hybrid) | doi:10.1093/nar/gkaa1055|pubme |
| RYBP | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:34316702|imex:IM-29168 |
| PIP | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |
| CSNK1A1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:33961781|imex:IM-29278| |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=54.3 + PDB: 2XRW, 2XS0 | pLDDT=54.3, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus / Nucleoplasm, Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. NFATC3 — Nuclear factor of activated T-cells, cytoplasmic 3，研究基础较多，新颖性有限。
2. 蛋白大小1075 aa，大小基本合适，可用于常规实验。

**风险/不确定性**:
1. PubMed 261 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=54.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 261 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q12968
- Protein Atlas: https://www.proteinatlas.org/ENSG00000072736-NFATC3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NFATC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q12968
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000072736-NFATC3/subcellular

![](https://images.proteinatlas.org/50665/757_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/50665/757_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/50665/761_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/50665/761_E11_2_red_green.jpg)
![](https://images.proteinatlas.org/50665/769_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/50665/769_E11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q12968-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
