---
type: protein-evaluation
gene: "BLMH"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## BLMH 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | BLMH / 无 |
| 蛋白名称 | Bleomycin hydrolase |
| 蛋白大小 | 455 aa / 52.6 kDa |
| UniProt ID | Q13867 |
| 评估日期 | 2026-06-03 |
| 数据采集时间 | 2026-06-03 03:38:51 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Nuclear bodies, Cyt... |
| 蛋白大小 | 10/10 | x1 | 10 | 455 aa / 52.6 kDa |
| 研究新颖性 | 6/10 | x5 | 30 | PubMed strict=45 篇 (41-60->6) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=98.0; PDB: 1CB5, 2CB5, ... |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: 3; Pfam: 1; IPR038765, IPR000169... |
| PPI 网络 | 10/10 | x3 | 30 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | -- | max +3 | 2.5 | PDB + AlphaFold 双源验证: +0.5; 多库定位一致 (3源): +0.5; STRING + IntAct 双源验证: +0.5; 结构域 + AlphaFold 质量: +0.5; PDB 多条目覆盖: +0.5 |
| **原始总分** | | | **144.5/180** | |
| **归一化总分 (/1.83)** | | | **79.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm; 额外: Nucleoplasm, Nuclear bodies, Cytosol | Supported |
| UniProt | Cytoplasm, Cytoplasmic granule | Swiss-Prot/TrEMBL |

**IF 图像说明**: HPA subcellular IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；核定位仍结合 HPA reliability、UniProt 和 GO-CC 综合判断。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- extracellular exosome (GO:0070062)
- nucleus (GO:0005634)

**结论**: 核定位证据较好，主要数据源支持核定位，但存在一定程度的其它亚细胞定位信号。

#### 3.2 蛋白大小评估

**评价**: 455 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 45 |
| PubMed broad count | 50 |

**关键文献**:
1. Association of GLOD4 with Alzheimer's Disease in Humans and Mice.. *Journal of Alzheimer's disease : JAD*. PMID: 39302370
2. Hyperhomocysteinemia and bleomycin hydrolase modulate the expression of mouse brain proteins involved in neurodegeneration.. *Journal of Alzheimer's disease : JAD*. PMID: 24496069
3. Deletion of the Homocysteine Thiolactone Detoxifying Enzyme Bleomycin Hydrolase, in Mice, Causes Memory and Neurological Deficits and Worsens Alzheimer's Disease-Related Behavioral and Biochemical Traits in the 5xFAD Model of Alzheimer's Disease.. *Journal of Alzheimer's disease : JAD*. PMID: 37718819
4. Design and Synthesis of Activity-Based Probes and Inhibitors for Bleomycin Hydrolase.. *Chemistry & biology*. PMID: 26256478
5. Effect of Bleomycin Hydrolase Expression in Tumor Tissue on the Therapeutic Effectiveness of Electrochemotherapy.. *Cancers*. PMID: 41514636

**评价**: 中等新颖性，有一定研究基础但仍有探索空间（PubMed 41-60篇）。新颖性评分 6/10。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 98.0 |
| 高置信度残基 (pLDDT>90) 占比 | 97.8% |
| 置信残基 (pLDDT 70-90) 占比 | 1.5% |
| 中等置信 (pLDDT 50-70) 占比 | 0.7% |
| 低置信 (pLDDT<50) 占比 | 0.0% |
| 有序区域 (pLDDT>70) 占比 | 99.3% |
| 可用 PDB 条目 | 1CB5, 2CB5, 7V5L, 7V5S, 7V5T, 7XF9 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold高质量预测（pLDDT=98.0），结构可信度高。三维结构评分 10/10。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR038765, IPR000169, IPR004134; Pfam: PF03051 |

**染色质调控潜力分析**: 存在 4 个已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score > 0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| NUDT12 | 0.869 | 0.850 | -- |
| CASP14 | 0.817 | 0.312 | -- |
| KERA | 0.746 | 0.743 | -- |
| CTSD | 0.687 | 0.321 | -- |
| TGM3 | 0.669 | 0.309 | -- |
| TPP2 | 0.634 | 0.000 | -- |
| APP | 0.615 | 0.553 | -- |
| FLG | 0.613 | 0.312 | -- |
| NPEPPS | 0.599 | 0.000 | -- |
| TMIGD1 | 0.588 | 0.000 | -- |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000261714.6 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| KBTBD7 | two hybrid pooling approach | pubmed:16189514|imex:IM-16520|mint:MINT-5217968 |
| TRIO | two hybrid pooling approach | pubmed:16169070|imex:IM-16517|mint:MINT-5217955 |
| Slc2a4 | anti tag coimmunoprecipitation | pubmed:16396496|mint:MINT-5218203 |
| APP | pull down | pubmed:11350084|imex:IM-20356 |
| USP53 | anti tag coimmunoprecipitation | imex:IM-12079|pubmed:19615732 |
| GABARAPL2 | anti tag coimmunoprecipitation | pubmed:20562859|imex:IM-15184 |
| CYP2C8 | two hybrid array | doi:10.1101/gr.114280.110|imex:IM-15153|pubmed:21163940 |
| ECSIT | two hybrid array | doi:10.1101/gr.114280.110|imex:IM-15153|pubmed:21163940 |
| MAST1 | two hybrid array | doi:10.1101/gr.114280.110|imex:IM-15153|pubmed:21163940 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15

**评价**: 互作网络丰富：STRING 15 预测 + IntAct 15 实验互作。PPI 评分 10/10。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=98.0 + PDB: 1CB5, 2CB5, 7V5L | pLDDT=98.0, v6 | 预测+实验 |
| 定位 | HPA | Nucleoplasm, Nuclear bodies | 单一来源 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0.5
**总分**: +2.5 / max +3

### 4. 总体评价

**归一化总分**: 79.0/100

**核心优势**:
1. 蛋白大小455 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。
2. AlphaFold高质量预测（pLDDT=98.0），结构可信度高。
3. 已有PDB实验结构：1CB5, 2CB5, 7V5L。
4. 存在 4 个已知结构域，有明确的结构-功能切入点。

**风险/不确定性**:
1. 暂无明显风险因素。

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能

### 5. 数据来源

- UniProt: https://www.uniprot.org/uniprotkb/Q13867
- Protein Atlas: https://www.proteinatlas.org/search/BLMH
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=BLMH
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13867
- STRING: https://string-db.org/network/9606.BLMH
- Packet data timestamp: 2026-06-03 03:38:51

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000108578-BLMH/subcellular

![](https://images.proteinatlas.org/39548/460_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/39548/460_G10_4_red_green.jpg)
![](https://images.proteinatlas.org/39548/465_G10_1_red_green.jpg)
![](https://images.proteinatlas.org/39548/465_G10_3_red_green.jpg)
![](https://images.proteinatlas.org/39548/467_G10_2_red_green.jpg)
![](https://images.proteinatlas.org/39548/467_G10_3_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13867-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
