---
type: protein-evaluation
gene: "FBXO24"
date: 2026-06-03
tags: [protein-scout, nuclear-protein, evaluation]
status: scored
---

## FBXO24 核蛋白评估报告 (Full Re-evaluation)

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | FBXO24 / FBX24 |
| 蛋白名称 | F-box only protein 24 |
| 蛋白大小 | 580 aa / 64.9 kDa |
| UniProt ID | O75426 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: 暂无HPA定位数据; UniProt: Mitochondrion; Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 580 aa / 64.9 kDa |
| 研究新颖性 | 10/10 | ×5 | 50 | PubMed strict=16 篇 (≤20→10) |
| 三维结构 | 7/10 | ×3 | 21 | AlphaFold v6 pLDDT=76.8; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR036047, IPR001810, IPR052866, IPR009091, IPR000 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 14 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **133.5/180** | |
| **归一化总分** | | | **74.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Mitochondrion; Nucleus | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号（image_status: no_image_detected）。核定位证据基于HPA subcellular localization注释、UniProt注释和GO-CC术语。

**GO Cellular Component**:
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- SCF ubiquitin ligase complex (GO:0019005)
- ubiquitin ligase complex (GO:0000151)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 16 |
| PubMed broad count | 16 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: FBX24 |

**关键文献**:
1. Targeted degradation of extracellular mitochondrial aspartyl-tRNA synthetase modulates immune responses.. *Nature communications*. PMID: 39039092
2. VRK2 targeting potentiates anti-PD-1 immunotherapy in hepatocellular carcinoma through MYC destabilization.. *Nature communications*. PMID: 41073389
3. FBXO24 deletion causes abnormal accumulation of membraneless electron-dense granules in sperm flagella and male infertility.. *eLife*. PMID: 39163107
4. Ivabradine induces RAD51 degradation, potentiating PARP inhibitor efficacy in non-germline BRCA pathogenic variant triple-negative breast cancer.. *Journal of translational medicine*. PMID: 40764992
5. Reciprocal Regulation Between the SCF(FBXO24) Ubiquitin E3 Ligase and FoxP1 Protein.. *bioRxiv : the preprint server for biology*. PMID: 40501863

**评价**: 极度新颖，几乎未被系统研究（PubMed ≤20篇）。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 76.8 |
| 高置信度残基 (pLDDT>90) 占比 | 32.9% |
| 置信残基 (pLDDT 70-90) 占比 | 40.5% |
| 中等置信 (pLDDT 50-70) 占比 | 12.8% |
| 低置信 (pLDDT<50) 占比 | 13.8% |
| 有序区域 (pLDDT>70) 占比 | 73.4% |
| 可用 PDB 条目 | 无 |


**PAE (Predicted Aligned Error)**:
![[Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO24/FBXO24-PAE.png]]

**评价**: AlphaFold 中等质量（pLDDT=76.8，有序区 73.4%），结构基本可用。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR036047, IPR001810, IPR052866, IPR009091, IPR000408; Pfam: PF12937, PF00415 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| SKP1 | 0.789 | 0.519 | — |
| NUDCD2 | 0.770 | 0.464 | — |
| CUL1 | 0.770 | 0.474 | — |
| RCC1 | 0.676 | 0.000 | — |
| FBXL12 | 0.525 | 0.050 | — |
| NUDCD3 | 0.516 | 0.140 | — |
| PRMT6 | 0.499 | 0.314 | — |
| SLC14A2 | 0.478 | 0.000 | — |
| FBXO28 | 0.445 | 0.000 | — |
| MAP3K6 | 0.440 | 0.000 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| HSP90AB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | imex:IM-17906|pubmed:22939624| |
| NUDCD2 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:25036637|imex:IM-22301 |
| Hacd3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| ENSP00000241071.6 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| HSF2 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| NUDCD3 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| NUDC | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| HSP90AA1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| FKBPL | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |
| STUB1 | psi-mi:"MI:0729"(luminescence based mammalian inte | pubmed:25036637|imex:IM-22301 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 14，IntAct interactions: 15
- 调控相关比例: 0 / 14 = 0%

**评价**: STRING 14 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=76.8 + PDB: 无 | pLDDT=76.8, v6 | 仅预测 |
| 定位 | UniProt + HPA | Mitochondrion; Nucleus / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 14 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐⭐

**核心优势**:
1. FBXO24 — F-box only protein 24，极度新颖，几乎未被系统研究（PubMed ≤20篇）。
2. 蛋白大小580 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 16 篇，研究基础极有限，功能注释不完整
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能


### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75426
- Protein Atlas: https://www.proteinatlas.org/ENSG00000106336-FBXO24/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=FBXO24
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75426
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleoplasm/FBXO24/FBXO24-PAE.png]]

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-06）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | O75426 |
| SMART | SM00256; |
| UniProt Domain [FT] | DOMAIN 36..82; /note="F-box"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU00080" |
| InterPro | IPR036047;IPR001810;IPR052866;IPR009091;IPR000408; |
| Pfam | PF12937;PF00415; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000106336-FBXO24/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| HSP90AB1 | Intact | false |
| KDM1A | Biogrid | false |
| NME1 | Biogrid | false |
| NUDCD2 | Intact | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
