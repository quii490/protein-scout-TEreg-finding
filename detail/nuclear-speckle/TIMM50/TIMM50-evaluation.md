---
type: protein-evaluation
gene: "TIMM50"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## TIMM50 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | TIMM50 / TIM50 |
| 蛋白名称 | Mitochondrial import inner membrane translocase subunit TIM50 |
| 蛋白大小 | 353 aa / 39.6 kDa |
| UniProt ID | Q3ZCQ8 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Mitochondria; UniProt: Mitochondrion inner membrane; Nucleus speckle |
| 蛋白大小 | 10/10 | ×1 | 10 | 353 aa / 39.6 kDa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=27 篇 (≤40→8) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=79.9; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004274, IPR036412, IPR023214, IPR050365; Pfam:  |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **123.5/180** | |
| **归一化总分** | | | **68.6/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Mitochondria | Supported |
| UniProt | Mitochondrion inner membrane; Nucleus speckle | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- endoplasmic reticulum (GO:0005783)
- Golgi apparatus (GO:0005794)
- mitochondrial inner membrane (GO:0005743)
- mitochondrion (GO:0005739)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- TIM23 mitochondrial import inner membrane translocase complex (GO:0005744)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 27 |
| PubMed broad count | 39 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: TIM50 |

**关键文献**:
1. Biochemical and neurophysiological effects of deficiency of the mitochondrial import protein TIMM50.. *eLife*. PMID: 39680434
2. Mitochondrial Protein Homeostasis and Cardiomyopathy.. *International journal of molecular sciences*. PMID: 35328774
3. Biochemical and neurophysiological effects of deficiency of the mitochondrial import protein TIMM50.. *bioRxiv : the preprint server for biology*. PMID: 38826427
4. Lactate-related gene signatures predict prognosis and immune profiles in esophageal squamous cell carcinoma.. *Scientific reports*. PMID: 40617965
5. Heart failure in patients is associated with downregulation of mitochondrial quality control genes.. *European journal of clinical investigation*. PMID: 37403271

**评价**: 非常新颖，仅有少数基础研究。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 79.9 |
| 高置信度残基 (pLDDT>90) 占比 | 47.6% |
| 置信残基 (pLDDT 70-90) 占比 | 30.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.5% |
| 低置信 (pLDDT<50) 占比 | 15.9% |
| 有序区域 (pLDDT>70) 占比 | 77.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 中等质量（pLDDT=79.9，有序区 77.6%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004274, IPR036412, IPR023214, IPR050365; Pfam: PF03031 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| TIMM17A | 0.999 | 0.630 | — |
| TIMM21 | 0.999 | 0.735 | — |
| TIMM23 | 0.999 | 0.881 | — |
| TIMM17B | 0.996 | 0.726 | — |
| TIMM44 | 0.985 | 0.154 | — |
| DNAJC19 | 0.973 | 0.162 | — |
| PAM16 | 0.972 | 0.498 | — |
| TOMM40 | 0.971 | 0.606 | — |
| TIMM23B | 0.946 | 0.840 | — |
| TIMM10 | 0.945 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| MAP3K3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| MAP3K14 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TRAF1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RELB | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK1 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| RIPK3 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| TAB2 | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |
| NFKBIA | psi-mi:"MI:0676"(tandem affinity purification) | pubmed:14743216|mint:MINT-5216 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 1 / 15 = 7%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 7%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=79.9 + PDB: 无 | pLDDT=79.9, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion inner membrane; Nucleus speckle / Nucleoplasm, Mitochondria | 一致 |
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
1. TIMM50 — Mitochondrial import inner membrane translocase subunit TIM50，非常新颖，仅有少数基础研究。
2. 蛋白大小353 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 27 篇，已有一定研究基础
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q3ZCQ8
- Protein Atlas: https://www.proteinatlas.org/ENSG00000105197-TIMM50/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=TIMM50
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q3ZCQ8
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (supported)。来源: https://www.proteinatlas.org/ENSG00000105197-TIMM50/subcellular

![](https://images.proteinatlas.org/48843/736_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48843/736_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48843/805_B12_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48843/805_B12_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/48843/864_H2_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/48843/864_H2_4_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q3ZCQ8-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
