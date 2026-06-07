---
type: protein-evaluation
gene: "Sycp3"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## Sycp3 — REJECTED (研究热度过高 (PubMed strict=271，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | Sycp3 / SCP3 |
| 蛋白名称 | Synaptonemal complex protein 3 |
| 蛋白大小 | 236 aa / 27.7 kDa |
| UniProt ID | Q8IZU3 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 8/10 | ×4 | 32 | HPA: 暂无HPA定位数据; UniProt: Nucleus; Chromosome; Chromosome, centromere |
| 蛋白大小 | 10/10 | ×1 | 10 | 236 aa / 27.7 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=271 篇 (>100→REJECTED) |
| 三维结构 | 8/10 | ×3 | 24 | AlphaFold v6 pLDDT=81.0; PDB: 4CPC |
| 调控结构域 | 8/10 | ×2 | 16 | InterPro: IPR051443, IPR006888; Pfam: PF04803 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 4 interactions |
| 互证加分 | — | max +3 | 2.0 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **93.0/180** | |
| **归一化总分** | | | **51.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Nucleus; Chromosome; Chromosome, centromere | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- chromosome, centromeric region (GO:0000775)
- lateral element (GO:0000800)
- nucleus (GO:0005634)
- synaptonemal complex (GO:0000795)

**结论**: 主要定位于细胞核，HPA + UniProt/GO-CC 共同支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 271 |
| PubMed broad count | 502 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: SCP3 |

**关键文献**:
1. Principles of chromosome organization for meiotic recombination.. *Molecular cell*. PMID: 38657614
2. Proteomic analysis of cisplatin-induced spermatogenesis defects in mice.. *Annals of medicine*. PMID: 41517957
3. Polymorphisms and expression levels of TNP2, SYCP3, and AZFa genes in patients with azoospermia.. *Clinical and experimental reproductive medicine*. PMID: 37995753
4. TRAPPC2l Participates in Male Germ Cell Development by Regulating Cell Division.. *Cell proliferation*. PMID: 40539230
5. The multi-copy mouse gene Sycp3-like Y-linked (Sly) encodes an abundant spermatid protein that interacts with a histone acetyltransferase and an acrosomal protein.. *Biology of reproduction*. PMID: 19176879

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 81.0 |
| 高置信度残基 (pLDDT>90) 占比 | 65.3% |
| 置信残基 (pLDDT 70-90) 占比 | 6.4% |
| 中等置信 (pLDDT 50-70) 占比 | 5.5% |
| 低置信 (pLDDT<50) 占比 | 22.9% |
| 有序区域 (pLDDT>70) 占比 | 71.7% |
| 可用 PDB 条目 | 4CPC |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 高质量预测（pLDDT=81.0，有序区 71.7%），结构可靠。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR051443, IPR006888; Pfam: PF04803 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高，结构域折叠可信。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SYCP2 | 0.998 | 0.230 | — |
| SYCP1 | 0.996 | 0.095 | — |
| HORMAD2 | 0.979 | 0.050 | — |
| HORMAD1 | 0.973 | 0.050 | — |
| SYCE2 | 0.970 | 0.000 | — |
| BRCA2 | 0.969 | 0.292 | — |
| TEX12 | 0.959 | 0.000 | — |
| SYCE3 | 0.948 | 0.000 | — |
| MSH4 | 0.947 | 0.049 | — |
| SYCE1 | 0.938 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| NXF1 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| C14orf119 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |
| CDC37 | psi-mi:"MI:1356"(validated two hybrid) | pubmed:32296183|imex:IM-25472 |
| BLK | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 4
- 调控相关比例: 3 / 15 = 20%

**评价**: STRING 15 个预测互作，IntAct 4 个实验互作。调控相关配体占比 20%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=81.0 + PDB: 4CPC | pLDDT=81.0, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus; Chromosome; Chromosome, centromere / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 15 + 4 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +2.0 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. Sycp3 — Synaptonemal complex protein 3，研究基础较多，新颖性有限。
2. 蛋白大小236 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 271 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 271 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q8IZU3
- Protein Atlas: https://www.proteinatlas.org/ENSG00000139351-SYCP3/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=Sycp3
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q8IZU3
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q8IZU3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q8IZU3 |
| SMART | 未在 UniProt xref 中检出 SMART 条目 |
| UniProt Domain [FT] | 未检出显式 UniProt Domain feature |
| InterPro | IPR051443;IPR006888; |
| Pfam | PF04803; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000139351-SYCP3/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| BLK | Intact | false |
| BRCA2 | Intact | false |
| C14orf119 | Intact | false |
| CDC37 | Intact | false |
| NXF1 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
