---
type: protein-evaluation
gene: "BRCC3"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BRCC3 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BRCC3 / BRCC36, C6.1A, CXorf53 |
| 蛋白名称 | Lys-63-specific deubiquitinase BRCC36 |
| 蛋白大小 | 316 aa / 36.1 kDa |
| UniProt ID | P46736 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:43:54 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | x4 | 36 | HPA: Nucleoplasm; UniProt: Nucleus, C... |
| 蛋白大小 | 10/10 | x1 | 10 | 316 aa / 36.1 kDa |
| 研究新颖性 | 4/10 | x5 | 20 | PubMed strict=76 篇 (61-80->4) |
| 三维结构 | 9/10 | x3 | 27 | AlphaFold v6 pLDDT=84.6; PDB: 6H3C, 6R8F, ... |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: 5; Pfam: 2; IPR040749, IPR000555... |
| PPI 网络 | 6/10 | x3 | 18 | STRING 0 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.0 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **129.0/180** | |
| **归一化总分 (/1.83)** | | | **70.5/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm | Supported |
| UniProt | Nucleus, Cytoplasm, Cytoplasm, cytoskeleton, spindle pole | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- BRCA1-A complex (GO:0070531)
- BRISC complex (GO:0070552)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- nuclear ubiquitin ligase complex (GO:0000152)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- spindle pole (GO:0000922)
- ubiquitin ligase complex (GO:0000151)

**结论**: 核定位证据充分，多个数据源一致支持核定位，定位特异性高。

#### 3.2 蛋白大小评估

**评价**: 316 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 76 |
| PubMed broad count | 139 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: BRCC36, C6.1A, CXorf53 |

**关键文献**:
1. BRCC3 Regulation of ALK2 in Vascular Smooth Muscle Cells: Implication in Pulmonary Hypertension.. *Circulation*. PMID: 38557054
2. BRCC3-Mediated NLRP3 Deubiquitylation Promotes Inflammasome Activation and Atherosclerosis in Tet2 Clonal Hematopoiesis.. *Circulation*. PMID: 37781816
3. BRISC-Mediated PPM1B-K63 Deubiquitination and Subsequent TGF-β Pathway Activation Promote High-Fat/High-Sucrose Diet-Induced Arterial Stiffness.. *Circulation research*. PMID: 39742393
4. Identification of BRCC3 and BRCA1 as Regulators of TAZ Stability and Activity.. *Cells*. PMID: 37887275
5. BRCC3 mediates inflammation and pyroptosis in cerebral ischemia/reperfusion injury by activating the NLRP6 inflammasome.. *CNS neuroscience & therapeutics*. PMID: 38544474

**评价**: 研究较多，新颖性一般（PubMed 61-80篇）。新颖性评分 4/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 84.6 |
| 高置信度残基 (pLDDT>90) 占比 | 72.8% |
| 置信残基 (pLDDT 70-90) 占比 | 7.9% |
| 中等置信 (pLDDT 50-70) 占比 | 3.2% |
| 低置信 (pLDDT<50) 占比 | 16.1% |
| 有序区域 (pLDDT>70) 占比 | 80.7% |
| 可用 PDB 条目 | 6H3C, 6R8F, 8PVY, 8PY2 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=84.6），结构可信度高。三维结构评分 9/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR040749, IPR000555, IPR050242, IPR037518, IPR033860; Pfam: PF18110, PF01398 |

**染色质调控潜力分析**: 存在 7 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作**: 暂无数据或查询失败。

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000358474.1 | luminescence based mammalian interactome | pubmed:37398436|imex:IM-29926 |
| SNAPC5 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| BABAM2 | anti bait coimmunoprecipitation | pubmed:17353931 |
| DDOST | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| BABAM1 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| ATP5PO | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| NDUFA10 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| BAG6 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| E2F5 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| MCM2 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |

**PPI 互证分析**:
- 仅 IntAct 有数据 (15 interactions)

**评价**: 互作网络中等：STRING 0 预测 + IntAct 15 实验互作。PPI 评分 6/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=84.6 + PDB: 6H3C, 6R8F, 8PVY | pLDDT=84.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleoplasm / Nucleus | 一致 |
| PPI | IntAct | 15 interactions | 单一来源 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.0 / max +3

### 4. 总体评价

**归一化总分**: 70.5/100

**核心优势**:
1. 蛋白大小316 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
2. AlphaFold高质量预测（pLDDT=84.6），结构可信度高。
3. 已有PDB实验结构：6H3C, 6R8F, 8PVY。
4. 存在 7 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 暂无明显风险因素。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/P46736
- Protein Atlas: https://www.proteinatlas.org/search/BRCC3
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BRCC3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P46736
- STRING: https://string-db.org/network/9606.BRCC3
- Packet data timestamp: 2026-06-03 03:43:54

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000185515-BRCC3/subcellular

![](https://images.proteinatlas.org/48737/791_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/48737/791_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/48737/794_C11_2_red_green.jpg)
![](https://images.proteinatlas.org/48737/794_C11_3_red_green.jpg)
![](https://images.proteinatlas.org/48737/798_C11_1_red_green.jpg)
![](https://images.proteinatlas.org/48737/798_C11_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P46736-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
