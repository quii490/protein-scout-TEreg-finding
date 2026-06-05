---
type: protein-evaluation
gene: "MAF"
date: 2026-06-03
tags: [protein-scout, rejected, evaluation]
status: rejected
---

## MAF — REJECTED (研究热度过高 (PubMed strict=2588，超过100篇阈值))

### 1. 基本信息

| 项目 | 内容 |
|------|------|
| 基因名 / 别名 | MAF |
| 蛋白名称 | Transcription factor Maf |
| 蛋白大小 | 373 aa / 38.5 kDa |
| UniProt ID | O75444 |
| 评估日期 | 2026-06-03 |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|------|------|------|--------|-------------|
| 核定位特异性 | 7/10 | ×4 | 28 | HPA: Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus, Vesicles; UniProt: Nucleus |
| 蛋白大小 | 10/10 | ×1 | 10 | 373 aa / 38.5 kDa |
| 研究新颖性 | 0/10 | ×5 | 0 | PubMed strict=2588 篇 (>100→REJECTED) |
| 三维结构 | 6/10 | ×3 | 18 | AlphaFold v6 pLDDT=59.3; PDB: 无 |
| 调控结构域 | 7/10 | ×2 | 14 | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008 |
| PPI 网络 | 3/10 | ×3 | 9 | STRING 15 partners; IntAct 0 interactions |
| 互证加分 | — | max +3 | 0.5 | PDB+AF+STRING+IntAct cross-validation |
| **原始总分** | | | **79.5/180** | |
| **归一化总分** | | | **44.2/100** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| Protein Atlas (IF) | Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus, Vesicles | Approved |
| UniProt | Nucleus | Swiss-Prot/TrEMBL |

HPA IF 图像已重新获取并嵌入（见下方 HPA IF 图像修正块）；此前“暂无/未可靠获取 IF”的表述为采集失败导致的误报。

**GO Cellular Component**:
- chromatin (GO:0000785)
- cytoplasm (GO:0005737)
- nucleus (GO:0005634)
- RNA polymerase II transcription regulator complex (GO:0090575)

**结论**: 主要核定位，HPA 可靠性良好，有辅助数据源支持。

#### 3.2 蛋白大小评估

**评价**: 大小适中（200-800 aa），适合常规生化实验和结构解析。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict count | 2588 |
| PubMed broad count | 7156 |
| 别名(未计入scoring) | 无 |

**关键文献**:
1. Molecular Pathogenesis of Multiple Myeloma: Clinical Implications.. *Hematology/oncology clinics of North America*. PMID: 38199896
2. A mechanistic basis of fast myofiber vulnerability to neuromuscular diseases.. *Cell reports*. PMID: 40632651
3. Blimp-1 and c-Maf regulate immune gene networks to protect against distinct pathways of pathobiont-induced colitis.. *Nature immunology*. PMID: 38609547
4. c-MAF-dependent perivascular macrophages regulate diet-induced metabolic syndrome.. *Science immunology*. PMID: 34597123
5. MAF amplification licenses ERα through epigenetic remodelling to drive breast cancer metastasis.. *Nature cell biology*. PMID: 37945904

**评价**: 研究基础较多，新颖性有限。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| AlphaFold 版本 | v6 |
| AlphaFold 平均 pLDDT | 59.3 |
| 高置信度残基 (pLDDT>90) 占比 | 24.4% |
| 置信残基 (pLDDT 70-90) 占比 | 3.2% |
| 中等置信 (pLDDT 50-70) 占比 | 17.4% |
| 低置信 (pLDDT<50) 占比 | 55.0% |
| 有序区域 (pLDDT>70) 占比 | 27.6% |
| 可用 PDB 条目 | 无 |

**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。

**评价**: AlphaFold 预测质量有限（pLDDT=59.3），有序残基占 27.6%。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|--------|
| InterPro/Pfam | InterPro: IPR004827, IPR004826, IPR046347, IPR013592, IPR008917; Pfam: PF03131, PF08383 |

**染色质调控潜力分析**: 存在已知结构域注释，可作为功能研究的结构基础。

#### 3.6 PPI 网络

**STRING 预测互作** (combined score >0.4):

| Partner | Combined Score | Experimental | 功能类别 |
|---------|---------------|--------------|---------|
| FOS | 0.998 | 0.753 | — |
| NFE2L2 | 0.998 | 0.397 | — |
| JUN | 0.993 | 0.110 | — |
| BACH2 | 0.993 | 0.184 | — |
| NFE2 | 0.986 | 0.184 | — |
| NFE2L1 | 0.970 | 0.184 | — |
| NEIL1 | 0.946 | 0.000 | — |
| NFE2L3 | 0.905 | 0.184 | — |
| PAX6 | 0.900 | 0.095 | — |
| CREB1 | 0.893 | 0.000 | — |

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
| 三维结构 | AlphaFold pLDDT=59.3 + PDB: 无 | pLDDT=59.3, v6 | 仅预测 |
| 定位 | UniProt + HPA | Nucleus / Nucleoplasm, Nuclear bodies; 额外: Golgi apparatus,  | 一致 |
| PPI | STRING + IntAct | 15 + 0 interactions | 数据有限 |

**互证加分明细**:
- PDB + AlphaFold 双源验证: +0
- 多库定位一致 (3源): +0.5
- STRING + IntAct 双源验证: +0
- 结构域 + AlphaFold 质量: +0
- PDB 多条目覆盖: +0
**总分**: +0.5 / max +3

### 4. 总体评价

**推荐等级**: ⭐⭐ (REJECTED)

**核心优势**:
1. MAF — Transcription factor Maf，研究基础较多，新颖性有限。
2. 蛋白大小373 aa，大小适中（200-800 aa），适合常规生化实验和结构解析。

**风险/不确定性**:
1. PubMed 2588 篇，研究热度过高（>100），不符合新颖性要求
2. AlphaFold 预测质量一般（pLDDT=59.3），需要更多实验结构验证

**下一步建议**:
- [ ] 查阅最新关键文献补充研究背景
- [ ] 获取 Protein Atlas IF 图像确认亚细胞定位
- [ ] 设计体外实验验证核定位及潜在调控功能
**该蛋白PubMed文献数 2588 > 100，研究热度过高，不符合novelty筛选标准。**

### 5. 数据来源
- UniProt: https://www.uniprot.org/uniprotkb/O75444
- Protein Atlas: https://www.proteinatlas.org/ENSG00000178573-MAF/subcellular
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=MAF
- AlphaFold: https://alphafold.ebi.ac.uk/entry/O75444
- STRING: https://string-db.org/network/9606.ENSP00000
- Data fetched live: 2026-06-03

<!-- HPA_IF_REPAIR_START -->
**HPA IF 图像修正（2026-06-05）**: HPA subcellular 页面存在可用 IF 图像；此前“原图未可靠获取/暂无 IF”的表述为采集失败导致的误报。HPA 定位: Nucleoplasm (approved)。来源: https://www.proteinatlas.org/ENSG00000178573-MAF/subcellular

![](https://images.proteinatlas.org/28289/2087_A1_1_red_green.jpg)
![](https://images.proteinatlas.org/28289/2087_A1_2_red_green.jpg)
![](https://images.proteinatlas.org/28289/2231_C6_12_red_green.jpg)
![](https://images.proteinatlas.org/28289/2231_C6_3_red_green.jpg)
![](https://images.proteinatlas.org/28289/286_E11_1_red_green.jpg)
![](https://images.proteinatlas.org/28289/286_E11_2_red_green.jpg)
<!-- HPA_IF_REPAIR_END -->

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-O75444-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
