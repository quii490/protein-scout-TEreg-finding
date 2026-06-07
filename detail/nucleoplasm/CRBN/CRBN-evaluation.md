---
type: protein-evaluation
gene: "CRBN"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## CRBN — REJECTED (研究热度过高 (PubMed strict=688，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | CRBN |
| 蛋白名称 | Protein cereblon |
| 蛋白大小 | 442 aa / 50.5 kDa |
| UniProt ID | Q96SW2 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: 暂无HPA定位数据; UniProt: Cytoplasm; Nucleus; Membrane |
| 蛋白大小 | 10/10 | x1 | 10 | 442 aa / 50.5 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=688 篇 (>100→REJECTED) |
| 三维结构 | 10/10 | x3 | 30 | AlphaFold v6 pLDDT=86.6; PDB: 4M91, 4TZ4, 5FQD, 5HXB, 5V3O, 6BN7, 6BN8 |
| 调控结构域 | 8/10 | x2 | 16 | InterPro: IPR034750, IPR003111, IPR046336, IPR015947, IPR004 |
| PPI 网络 | 2/10 | x3 | 6 | STRING 0 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 2.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **92.5/180** | |
| **归一化总分** | | | **51.4/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | 暂无HPA定位数据 | 暂无 |
| UniProt | Cytoplasm; Nucleus; Membrane | Swiss-Prot/TrEMBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- Cul4A-RING E3 ubiquitin ligase complex (GO:0031464)
- cytoplasm (GO:0005737)
- cytosol (GO:0005829)
- membrane (GO:0016020)
- nucleus (GO:0005634)
- perinuclear region of cytoplasm (GO:0048471)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 688 |
| PubMed broad count | 1060 |
| 别名(未计入scoring) |  |

**关键文献**:
1. Identification of a primary target of thalidomide teratogenicity.. *Science (New York, N.Y.)*. PMID: 20223979
2. Molecular glue CELMoD compounds are regulators of cereblon conformation.. *Science (New York, N.Y.)*. PMID: 36378961
3. Rapid and direct control of target protein levels with VHL-recruiting dTAG molecules.. *Nature communications*. PMID: 32948771
4. From Thalidomide to Rational Molecular Glue Design for Targeted Protein Degradation.. *Annual review of pharmacology and toxicology*. PMID: 37585660
5. Developments of CRBN-based PROTACs as potential therapeutic agents.. *European journal of medicinal chemistry*. PMID: 34411892

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 86.6 |
| 高置信度残基 (pLDDT>90) 占比 | 71.7% |
| 置信残基 (pLDDT 70-90) 占比 | 13.8% |
| 中等置信 (pLDDT 50-70) 占比 | 5.7% |
| 低置信 (pLDDT<50) 占比 | 8.8% |
| 有序区域 (pLDDT>70) 占比 | 85.5% |
| 可用 PDB 条目 | 4M91, 4TZ4, 5FQD, 5HXB, 5V3O, 6BN7, 6BN8, 6BN9, 6BNB, 6BOY |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: PDB实验结构 + AlphaFold极高置信度（pLDDT=86.6），结构可信度极高。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR034750, IPR003111, IPR046336, IPR015947, IPR004910; Pfam: PF02190, PF03226 |

**染色质调控潜力分析**: 多个已知结构域注释，AlphaFold预测质量高。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| — | — | — | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| — | — | — |

**PPI 互证分析**:
- 无PPI数据
- STRING partners: 0，IntAct interactions: 0
- 调控相关比例: 0 / 0 = 0%

**评价**: STRING 0 个预测互作，IntAct 0 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=86.6 + PDB: 4M91, 4TZ4, 5FQD, 5HXB, 5V3O,  | pLDDT=86.6, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Cytoplasm; Nucleus; Membrane / 暂无HPA定位数据 | 一致 |
| PPI | STRING + IntAct | 0 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (2源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0.5
- PDB 多条目覆盖 (>=3): +1.0
**总分**: +2.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐⭐ (REJECTED)

**核心优势**:
1. CRBN -- Protein cereblon，研究基础较多，新颖性有限。
2. 蛋白大小442 aa，大小适中（200-800 aa），适合常规生化实验。

**风险/不确定性**:
1. PubMed 688 篇，研究热度过高（>100），不符合新颖性要求
2. 结构数据质量可接受

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 688 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q96SW2
- Protein Atlas: https://www.proteinatlas.org/ENSG00000113851-CRBN/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=CRBN
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q96SW2
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q96SW2-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->

<!-- DOMAIN_HUMANPPI_REPAIR_START -->
## Domain/SMART 与 humanPPI 补充（2026-06-07）

### SMART / UniProt domain
| Source | Data |
|---|---|
| UniProt | Q96SW2 |
| SMART | SM00464; |
| UniProt Domain [FT] | DOMAIN 81..319; /note="Lon N-terminal"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01123"; DOMAIN 318..426; /note="CULT"; /evidence="ECO:0000255\|PROSITE-ProRule:PRU01124" |
| InterPro | IPR034750;IPR003111;IPR046336;IPR015947;IPR004910; |
| Pfam | PF02190;PF03226; |

### humanPPI / HPA Interaction
Source: https://www.proteinatlas.org/ENSG00000113851-CRBN/interaction

| Partner | Datasets | AF3/HPA structure |
|---|---|:--:|
| COPS5 | Intact, Biogrid | true |
| COPS6 | Intact, Biogrid | true |
| CSNK1A1 | Intact, Biogrid | true |
| CUL4A | Intact, Biogrid | true |
| DDB1 | Intact, Biogrid, Opencell | true |
| RBX1 | Intact, Biogrid | true |
| AGO2 | Biogrid | false |
| APP | Biogrid | false |
<!-- DOMAIN_HUMANPPI_REPAIR_END -->
