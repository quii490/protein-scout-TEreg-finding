---
type: protein-evaluation
gene: "DACH1"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## DACH1 — REJECTED (研究热度过高 (PubMed strict=173，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | DACH1 / DACH |
| 蛋白名称 | Dachshund homolog 1 |
| 蛋白大小 | 758 aa / 78.6 kDa |
| UniProt ID | Q9UI36 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | x4 | 28 | HPA: Nucleoplasm, Nuclear speckles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | x1 | 10 | 758 aa / 78.6 kDa |
| 研究新颖性 | 0/10 | x5 | 0 | PubMed strict=173 篇 (>100->REJECTED) |
| 三维结构 | 6/10 | x3 | 18 | AlphaFold v6 pLDDT=57.2; PDB: 1L8R |
| 调控结构域 | 7/10 | x2 | 14 | InterPro: IPR052417, IPR009061, IPR003380, IPR037000; Pfam:  |
| PPI 网络 | 3/10 | x3 | 9 | STRING 15 partners; IntAct 15 interactions |
| 互证加分 | — | max +3 | 1.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **80.5/180** | |
| **归一化总分** | | | **44.7/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear speckles | Supported |
| UniProt | Nucleus | Swiss-Prot/TremBL |

**IF 图像状态**: HPA未检测到可靠IF图像信号。定位证据基于HPA/UniProt/GO-CC注释。

**GO Cellular Component**:
- cytosol (GO:0005829)
- Golgi apparatus (GO:0005794)
- nuclear speck (GO:0016607)
- nucleoplasm (GO:0005654)
- nucleus (GO:0005634)
- transcription regulator complex (GO:0005667)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 173 |
| PubMed broad count | 349 |
| 别名(未计入scoring) | Aliases observed but not used for scoring: DACH |

**关键文献**:
1. Genetic variants associated with longitudinal changes in brain structure across the lifespan.. *Nature neuroscience*. PMID: 35383335
2. Long non-coding RNAs: From disease code to drug role.. *Acta pharmaceutica Sinica. B*. PMID: 33643816
3. The DACH1 Gene Transcriptional Activation and Protein Degradation Mediated by Transactivator Tas of Prototype Foamy Virus.. *Viruses*. PMID: 37766305
4. Synergistic regulation of DACH1 stability by acetylation and deubiquitination promotes colorectal cancer progression.. *Cell death & disease*. PMID: 40389405
5. Transcriptome-wide association analysis identifies DACH1 as a kidney disease risk gene that contributes to fibrosis.. *The Journal of clinical investigation*. PMID: 33998598

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 57.2 |
| 高置信度残基 (pLDDT>90) 占比 | 23.2% |
| 置信残基 (pLDDT 70-90) 占比 | 3.6% |
| 中等置信 (pLDDT 50-70) 占比 | 13.1% |
| 低置信 (pLDDT<50) 占比 | 60.2% |
| 有序区域 (pLDDT>70) 占比 | 26.8% |
| 可用 PDB 条目 | 1L8R |

**PAE**: PAE图像下载跳过（快速standard evaluation）。结构判断基于 AlphaFold pLDDT 统计。

**评价**: AlphaFold 预测质量有限（pLDDT=57.2），有序残基占 26.8%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR052417, IPR009061, IPR003380, IPR037000; Pfam: PF02437 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| EYA1 | 0.942 | 0.300 | — |
| SIX1 | 0.939 | 0.077 | — |
| SMAD4 | 0.927 | 0.292 | — |
| SIX6 | 0.884 | 0.095 | — |
| DACH2 | 0.847 | 0.757 | — |
| EYA2 | 0.798 | 0.300 | — |
| PAX3 | 0.788 | 0.071 | — |
| JUN | 0.787 | 0.584 | — |
| MYF5 | 0.746 | 0.000 | — |
| SIX4 | 0.724 | 0.071 | — |

**实验验证互作** (IntAct):

| Partner | 方法 | PMID |
|---------|------|------|
| ENSP00000482245.1 | psi-mi:"MI:0397"(two hybrid array) | imex:IM-23318|pubmed:25416956 |
| NAGK | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| UBE2I | psi-mi:"MI:0398"(two hybrid pooling approach) | pubmed:16189514|imex:IM-16520| |
| Six6 | psi-mi:"MI:0096"(pull down) | pubmed:12130660 |
| Ncor1 | psi-mi:"MI:0096"(pull down) | pubmed:12130660 |
| Hdac3 | psi-mi:"MI:0096"(pull down) | pubmed:12130660 |
| Sin3a | psi-mi:"MI:0096"(pull down) | pubmed:12130660 |
| Eya3 | psi-mi:"MI:0019"(coimmunoprecipitation) | pubmed:14628042 |
| WDR83 | psi-mi:"MI:0007"(anti tag coimmunoprecipitation) | pubmed:28514442|doi:10.1038/na |
| FGF12 | psi-mi:"MI:0397"(two hybrid array) | pubmed:32296183|imex:IM-25472 |

**PPI 互证分析**:
- STRING + IntAct 均有数据
- STRING partners: 15，IntAct interactions: 15
- 调控相关比例: 0 / 15 = 0%

**评价**: STRING 15 个预测互作，IntAct 15 个实验互作。调控相关配体占比 0%。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold pLDDT=57.2 + PDB: 1L8R | pLDDT=57.2, v6 | 预测+实验 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear speckles | 一致 |
| PPI | STRING + IntAct | 15 + 15 interactions | 数据充分 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0.5
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0.5
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +1.5 / max +3

### 4. 总体评价

**推荐等级**: ** (REJECTED)

**核心优势**:
1. DACH1 -- Dachshund homolog 1，研究基础较多，新颖性有限。
2. 蛋白大小758 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 173 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=57.2），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 173 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/Q9UI36
- Protein Atlas: https://www.proteinatlas.org/ENSG00000276644-DACH1/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=DACH1
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q9UI36
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03
