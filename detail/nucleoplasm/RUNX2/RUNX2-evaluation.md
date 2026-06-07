---
type: protein-evaluation
gene: "RUNX2"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RUNX2 — REJECTED (研究热度过高 (PubMed strict=7994，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RUNX2 / AML3, CBFA1, OSF2, PEBP2A |
| 蛋白名称 | Runt-related transcription factor 2 |
| 蛋白大小 | 521 aa / 56.6 kDa |
| UniProt ID | Q13950 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm; UniProt: Nucleus; Cytoplasm |
| 蛋白大小 | 10/10 | ×1 | 10 | 521 aa / 56.6 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=7994 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=58.6; PDB: 6VG8, 6VGD, 6VGE, 6VGG |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR000040, IPR008967, IPR012346, IPR013524, IPR027 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **81.0/180** | |
| **归一化总分** | | | **45.0/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm | Enhanced |
| UniProt | Nucleus; Cytoplasm | Swiss-Prot/TrEMBL |

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

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 7994 |
| PubMed broad count | 12987 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: AML3, CBFA1, OSF2, PEBP2A |

**关键文献**:
1. Regulation of Proliferation, Differentiation and Functions of Osteoblasts by Runx2.. *International journal of molecular sciences*. PMID: 30987410
2. RUNX2 is stabilised by TAZ and drives pulmonary artery calcification and lung vascular remodelling in pulmonary hypertension due to left heart disease.. *The European respiratory journal*. PMID: 39542509
3. Regulation of Skeletal Development and Maintenance by Runx2 and Sp7.. *International journal of molecular sciences*. PMID: 39337587
4. Post-translational Regulation of Runx2 in Bone and Cartilage.. *Journal of dental research*. PMID: 19734454
5. Runx2 and dental development.. *European journal of oral sciences*. PMID: 17026500

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 58.6 |
| 高置信度残基 (pLDDT>90) 占比 | 22.1% |
| 置信残基 (pLDDT 70-90) 占比 | 8.3% |
| 中等置信 (pLDDT 50-70) 占比 | 14.2% |
| 低置信 (pLDDT<50) 占比 | 55.5% |
| 有序区域 (pLDDT>70) 占比 | 30.4% |
| 可用 PDB 条目 | 6VG8, 6VGD, 6VGE, 6VGG |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=58.6），有序残基占 30.4%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR000040, IPR008967, IPR012346, IPR013524, IPR027384; Pfam: PF00853, PF08504 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| CBFB | 0.999 | 0.988 | — |
| HDAC4 | 0.997 | 0.637 | — |
| BGLAP | 0.996 | 0.246 | — |
| MSX2 | 0.995 | 0.300 | — |
| DLX5 | 0.990 | 0.000 | — |
| SMURF1 | 0.988 | 0.473 | — |
| FOS | 0.987 | 0.510 | — |
| BMP2 | 0.982 | 0.000 | — |
| SOX9 | 0.980 | 0.541 | — |
| SP7 | 0.977 | 0.067 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 仅STRING预测
- STRING partners: 15，IntAct interactions: 0
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=58.6 + PDB: 6VG8, 6VGD, 6VGE, 6VGG | pLDDT=58.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Cytoplasm / Nucleoplasm | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. RUNX2 — Runt-related transcription factor 2，研究基础较多，新颖性有限。
2. 蛋白大小521 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 7994 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=58.6），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 7994 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q13950
- Protein Atlas: https://www.proteinatlas.org/ENSG00000124813-RUNX2/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RUNX2
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q13950
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (enhanced)。来源: https://www.proteinatlas.org/ENSG00000124813-RUNX2/subcellular

![](https://images.proteinatlas.org/22040/192_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/22040/192_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/22040/193_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/22040/193_E5_2_red_green.jpg)
![](https://images.proteinatlas.org/22040/194_E5_1_red_green.jpg)
![](https://images.proteinatlas.org/22040/194_E5_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q13950-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q13950 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | DOMAIN 101..229; /note="Runt"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00399" |
| InterPro | IPR000040;IPR008967;IPR012346;IPR013524;IPR027384;IPR013711;IPR016554; |
| Pfam | PF00853;PF08504; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000124813-RUNX2/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PIN1 | Intact, Biogrid | true |
| UBTF | Intact, Biogrid | true |
| CBFB | Biogrid | false |
| DTX2 | Biogrid | false |
| EP300 | Biogrid | false |
| FHL2 | Biogrid | false |
| FOS | Biogrid | false |
| HDAC1 | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
