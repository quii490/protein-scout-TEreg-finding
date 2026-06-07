---
type: protein-evaluation
gene: "RORC"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## RORC — REJECTED (研究热度过高 (PubMed strict=444，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | RORC / NR1F3, RORG, RZRG |
| 蛋白名称 | Nuclear receptor ROR-gamma |
| 蛋白大小 | 518 aa / 58.2 kDa |
| UniProt ID | P51449 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA: Nuclear bodies; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 518 aa / 58.2 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=444 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | ×3 | 30 | AlphaFold v6 pLDDT=74.2; PDB: 3B0W, 3KYT, 3L0J, 3L0L, 4NB6, 4NIE, 4QM0 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR035500, IPR044101, IPR000536, IPR001723, IPR003 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **101.5/180** | |
| **归一化总分** | | | **56.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nuclear bodies | Supported |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- nuclear body (GO:0016604)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)

**结论**: 多个独立数据源一致确认核定位，HPA可靠性高，核定位证据充分。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 444 |
| PubMed broad count | 1520 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: NR1F3, RORG, RZRG |

**关键文献**:
1. Multi-omics approaches for the understanding of therapeutic mechanism for Huang-Qi-Long-Dan Granule against ischemic stroke.. *Pharmacological research*. PMID: 38782148
2. Multimodal single-cell analyses reveal mechanisms of perianal fistula in diverse patients with Crohn's disease.. *Med (New York, N.Y.)*. PMID: 38663404
3. PRDM16-dependent antigen-presenting cells induce tolerance to gut antigens.. *Nature*. PMID: 40228524
4. Single-cell epigenetic, transcriptional, and protein profiling of latent and active HIV-1 reservoir revealed that IKZF3 promotes HIV-1 persistence.. *Immunity*. PMID: 37922905
5. LAMP2-FLOT2 interaction enhances autophagosome-lysosome fusion to protect the septic heart in response to ILC2.. *Autophagy*. PMID: 40066518

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 74.2 |
| 高置信度残基 (pLDDT>90) 占比 | 55.2% |
| 置信残基 (pLDDT 70-90) 占比 | 10.0% |
| 中等置信 (pLDDT 50-70) 占比 | 6.8% |
| 低置信 (pLDDT<50) 占比 | 28.0% |
| 有序区域 (pLDDT>70) 占比 | 65.2% |
| 可用 PDB 条目 | 3B0W, 3KYT, 3L0J, 3L0L, 4NB6, 4NIE, 4QM0, 4S14, 4WLB, 4WPF |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构（3B0W, 3KYT, 3L0J, 3L0L, 4NB6, 4NIE, 4QM0, 4S14, 4WLB, 4WPF）+ AlphaFold极高置信度预测（pLDDT=74.2），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR035500, IPR044101, IPR000536, IPR001723, IPR003079; Pfam: PF00104, PF00105 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOXP3 | 0.987 | 0.301 | — |
| NCOR2 | 0.958 | 0.900 | — |
| NCOA1 | 0.947 | 0.934 | — |
| RORB | 0.935 | 0.329 | — |
| RORA | 0.934 | 0.000 | — |
| IL17A | 0.933 | 0.093 | — |
| NCOA2 | 0.920 | 0.907 | — |
| ARNTL | 0.912 | 0.534 | — |
| NRIP1 | 0.910 | 0.900 | — |
| TBX21 | 0.906 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=74.2 + PDB: 3B0W, 3KYT, 3L0J, 3L0L, 4NB6,  | pLDDT=74.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nuclear bodies | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (≥3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. RORC — Nuclear receptor ROR-gamma，研究基础较多，新颖性有限。
2. 蛋白大小518 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 444 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 444 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/P51449
- Protein Atlas: https://www.proteinatlas.org/ENSG00000143365-RORC/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=RORC
- AlphaFold: https://alphafold.ebi.ac.uk/entry/P51449
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nuclear bodies (supported)。来源: https://www.proteinatlas.org/ENSG00000143365-RORC/subcellular

![](https://images.proteinatlas.org/65620/1337_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65620/1337_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65620/1338_C7_1_blue_red_green.jpg)
![](https://images.proteinatlas.org/65620/1338_C7_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65620/1536_B11_2_blue_red_green.jpg)
![](https://images.proteinatlas.org/65620/1536_B11_3_blue_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-P51449-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | P51449 |
| SMART | SM00430;SM00399; |
| UniProt Domain [FT] | DOMAIN 269..508; /note="NR LBD"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01189" |
| InterPro | IPR035500;IPR044101;IPR000536;IPR001723;IPR003079;IPR001628;IPR013088; |
| Pfam | PF00104;PF00105; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000143365-RORC/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| PSMC5 | Intact, Biogrid | true |
| BMAL1 | Biogrid | false |
| CLOCK | Biogrid | false |
| CUL4B | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
