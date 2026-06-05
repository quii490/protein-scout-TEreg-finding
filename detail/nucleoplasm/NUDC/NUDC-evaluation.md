---
type: protein-evaluation
gene: "NUDC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## NUDC — REJECTED (研究热度过高 (PubMed strict=129，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | NUDC |
| 蛋白名称 | Nuclear migration protein nudC |
| 蛋白大小 | 331 aa / 38.2 kDa |
| UniProt ID | Q9Y266 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Cytosol; UniProt: Cytoplasm, cytoskeleton; Nucleus; Cytoplasm, cytoskeleton, s |
| 蛋白大小 | 10/10 | ×1 | 10 | 331 aa / 38.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=129 篇 (>100→REJECTED) |
| 三维结构 | 9/10 | ×3 | 27 | AlphaFold v6 pLDDT=81.4; PDB: 3QOR, 7NDX |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR007052, IPR008978, IPR032572, IPR037898, IPR025 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.0/180** | |
| **归一化总分** | | | **51.1/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Cytosol | Uncertain |
| UniProt | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm, cytoskeleton, spindle; Midbody | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- microtubule (GO:0005874)
- midbody (GO:0030496)
- mitotic spindle (GO:0072686)
- nucleoplasm (GO:0005654)
- spindle (GO:0005819)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 129 |
| PubMed broad count | 166 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. The nuclear migration gene NudC and human hematopoiesis.. *Leukemia & lymphoma*. PMID: 11342328
2. Emerging roles of NudC family: from molecular regulation to clinical implications.. *Science China. Life sciences*. PMID: 26965524
3. NUDC is critical for rod photoreceptor function, maintenance, and survival.. *FASEB journal : official publication of the Federation of American Societies for Experimental Biology*. PMID: 38441532
4. Transcriptome Analysis and the Prognostic Role of NUDC in Diffuse and Intestinal Gastric Cancer.. *Technology in cancer research & treatment*. PMID: 34060350
5. NUDC is critical for rod photoreceptor function, maintenance, and survival.. *bioRxiv : the preprint server for biology*. PMID: 38076848

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.4 |
| 高置信度残基 (pLDDT>90) 占比 | 48.9% |
| 置信残基 (pLDDT 70-90) 占比 | 29.0% |
| 中等置信 (pLDDT 50-70) 占比 | 11.5% |
| 低置信 (pLDDT<50) 占比 | 10.6% |
| 有序区域 (pLDDT>70) 占比 | 77.9% |
| 可用 PDB 条目 | 3QOR, 7NDX |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3QOR, 7NDX）+ AlphaFold高质量预测（pLDDT=81.4），结构可信度高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR007052, IPR008978, IPR032572, IPR037898, IPR025934; Pfam: PF04969, PF16273, PF14050 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAFAH1B1 | 0.996 | 0.778 | — |
| PLK1 | 0.990 | 0.292 | — |
| DNAJB1 | 0.967 | 0.957 | — |
| NDE1 | 0.941 | 0.000 | — |
| NDEL1 | 0.940 | 0.000 | — |
| DYNC1H1 | 0.937 | 0.095 | — |
| CLIP1 | 0.892 | 0.000 | — |
| CLASP2 | 0.889 | 0.000 | — |
| INCENP | 0.889 | 0.000 | — |
| SGO1 | 0.888 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| CALM1 | psi-mi:"MI:0004"(affinity chromatography technolog | pubmed:16512683|imex:IM-19867 |
| HLA-C | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ARF6 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| LXN | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| ATG5 | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| DGKE | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| TNFRSF10D | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| HLA-B | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |
| VHL | psi-mi:"MI:0006"(anti bait coimmunoprecipitation) | pubmed:17353931 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.4 + PDB: 3QOR, 7NDX | pLDDT=81.4, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm, cytoskeleton; Nucleus; Cytoplasm, cytos / Cytosol | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. NUDC — Nuclear migration protein nudC，研究基础较多，新颖性有限。
2. 蛋白大小331 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 129 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 129 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9Y266
- Protein Atlas: https://www.proteinatlas.org/ENSG00000090273-NUDC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=NUDC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9Y266
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Cytosol (uncertain)。来源: https://www.proteinatlas.org/ENSG00000090273-NUDC/subcellular

![](https://images.proteinatlas.org/27183/212_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27183/212_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27183/213_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27183/213_F12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/27183/214_F12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/27183/214_F12_2_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q9Y266-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
