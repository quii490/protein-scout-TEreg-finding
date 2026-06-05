---
type: protein-evaluation
gene: "PABPN1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## PABPN1 — REJECTED (研究热度过高 (PubMed strict=280，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | PABPN1 / PAB2, PABP2 |
| 蛋白名称 | Polyadenylate-binding protein 2 |
| 蛋白大小 | 306 aa / 32.7 kDa |
| UniProt ID | Q86U42 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus; Cytoplasm; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 306 aa / 32.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=280 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=67.9; PDB: 3B4D, 3B4M, 3UCG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR012677, IPR035979, IPR000504; Pfam: PF00076 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.5/180** | |
| **归一化总分** | | | **45.3/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Supported |
| UniProt | Nucleus; Cytoplasm; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nuclear inclusion body (GO:0042405)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- ribonucleoprotein complex (GO:1990904)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 280 |
| PubMed broad count | 318 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: PAB2, PABP2 |

**关键文献**:
1. Targeting PGE2 mediated senescent neuron improves tumor therapy.. *Neuro-oncology*. PMID: 39963753
2. PABPN1 Couples the Polyadenylation and Translation of Maternal Transcripts to Mouse Oocyte Meiotic Maturation.. *Advanced science (Weinheim, Baden-Wurttemberg, Germany)*. PMID: 40265969
3. BiFC and FACS-based CRISPR screening revealed that QKI promotes PABPN1 LLPS in colorectal cancer cells.. *Protein & cell*. PMID: 40052530
4. Oculopharyngeal Muscular Dystrophy.. **. PMID: 20301305
5. PABPN1-C5 axis promotes hepatocellular carcinoma progression via NF-κB activation.. *Oncogene*. PMID: 40721660

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 67.9 |
| 高置信度残基 (pLDDT>90) 占比 | 26.1% |
| 置信残基 (pLDDT 70-90) 占比 | 14.4% |
| 中等置信 (pLDDT 50-70) 占比 | 35.3% |
| 低置信 (pLDDT<50) 占比 | 24.2% |
| 有序区域 (pLDDT>70) 占比 | 40.5% |
| 可用 PDB 条目 | 3B4D, 3B4M, 3UCG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=67.9），有序残基占 40.5%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR012677, IPR035979, IPR000504; Pfam: PF00076 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| PAPOLA | 0.991 | 0.305 | — |
| ELAVL1 | 0.991 | 0.000 | — |
| BCL2L2-PABPN1 | 0.989 | 0.900 | — |
| NCBP2 | 0.988 | 0.627 | — |
| ZFC3H1 | 0.980 | 0.126 | — |
| NCBP1 | 0.978 | 0.499 | — |
| PABPC1 | 0.956 | 0.395 | — |
| SRSF1 | 0.946 | 0.301 | — |
| PABPC4 | 0.934 | 0.181 | — |
| U2AF2 | 0.929 | 0.162 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| Mylk | psi-mi:"MI:0018"(two hybrid) | pubmed:15102471 |
| - | psi-mi:"MI:0096"(pull down) | pubmed:23902751|imex:IM-21740 |
| glgB | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| Q81XY2 | psi-mi:"MI:0398"(two hybrid pooling approach) | imex:IM-13779|pubmed:20711500 |
| GABARAPL2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| GABARAPL1 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:20562859|imex:IM-15184 |
| NS1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |
| RB1 | psi-mi:"MI:0034"(display technology) | pubmed:20195357|imex:IM-20475 |
| CUL5 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:21145461|imex:IM-18651| |
| NS | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:22810585|imex:IM-17331 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=67.9 + PDB: 3B4D, 3B4M, 3UCG | pLDDT=67.9, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm; Nucleus speckle / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. PABPN1 — Polyadenylate-binding protein 2，研究基础较多，新颖性有限。
2. 蛋白大小306 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 280 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=67.9），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 280 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q86U42
- Protein Atlas: https://www.proteinatlas.org/ENSG00000100836-PABPN1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=PABPN1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86U42
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000100836-PABPN1/subcellular

![](https://images.proteinatlas.org/637/11_B10_1_red_green.jpg)
![](https://images.proteinatlas.org/637/11_B10_2_red_green.jpg)
![](https://images.proteinatlas.org/637/1841_F8_2_red_green.jpg)
![](https://images.proteinatlas.org/637/1841_F8_4_red_green.jpg)
![](https://images.proteinatlas.org/637/1899_A4_1_red_green.jpg)
![](https://images.proteinatlas.org/637/1899_A4_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86U42-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
