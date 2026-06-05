---
type: protein-evaluation
gene: "SFR1"
date: 2026-06-02
tags: [protein-scout, nucleus-cytoplasm, evaluation]
status: scored
pm: 40
---

## SFR1 核蛋白评估报告

### 1. 基本信息

| 项目 | 内容 |
|---|---|
| 基因名 / 别名 | SFR1 / C10orf78, MEI5, MEIR5 |
| 蛋白全称 | Swi5-dependent recombination DNA repair protein 1 homolog |
| 蛋白大小 | 245 aa / 28.3 kDa |
| UniProt ID | Q86XK3 |
| AlphaFold | AF-Q86XK3-F1 (v6) |

### 2. 评分总览

| 维度 | 得分 | 满分 | 加权后 | 关键证据摘要 |
|---|---|---|---|---|
| 核定位特异性 | 8/10 | ×4 | **32** | UniProt Nucleus (ECO:0000269 实验); HPA Supported Nucleoli rim + Nucleoplasm + Centrosome; GO nucleoplasm IDA + nucleus IDA |
| 蛋白大小 | 10/10 | ×1 | **10** | 245 aa，理想范围 |
| 研究新颖性 | 8/10 | ×5 | **40** | PubMed strict=40，≤40 档，高新颖性 |
| 三维结构 | 4/10 | ×3 | **12** | 无 PDB 结构; AF mean pLDDT 66.9, 31.0% <50 |
| 调控结构域 | 3/10 | ×2 | **6** | SWI5-SFR1 复合体; DNA 修复功能，非经典染色质调控 |
| PPI 网络 | 6/10 | ×3 | **18** | STRING 15 + IntAct 15; SWI5 + RAD51 同源重组网络; ESR1 互作 |
| 互证加分 | -- | -- | **+0.5** | HPA IF + UniProt 实验 + GO IDA 三源定位一致 (+0.5) |
| **加权总分** | | | **118/180**** | |
| **归一化总分 (÷1.83)** | | | **64.5/100**** | |

### 3. 详细分析

#### 3.1 核定位证据

| 来源 | 定位 | 可信度 |
|------|------|--------|
| UniProt | Nucleus (ECO:0000269) | 实验级 |
| GO-CC | nucleoplasm (GO:0005654, IDA:HPA); nucleolus (GO:0005730, IDA:HPA); centrosome (GO:0005813, IDA:HPA); nucleus (GO:0005634, IDA); Swi5-Sfr1 complex (GO:0032798, IDA) | 实验级 |
| HPA IF | Supported reliability; Nucleoli rim (main) + Nucleoplasm + Centrosome (additional) | 中等可信度 |

**HPA IF 状态**: Supported 级别可信度，多细胞系显示 Nucleoli rim 主定位，附加 Nucleoplasm + Centrosome。UniProt 实验级 (ECO:0000269) 支持 Nucleus。

**结论**: 核定位高可信度，HPA + UniProt 实验级 + GO IDA 三源一致。核仁 rim + 核质为主，centrosome 为附加定位。

#### 3.2 蛋白大小评估

**评价**: 245 aa (28.3 kDa)，处于理想实验范围 (150-400)。

#### 3.3 研究现状

| 指标 | 数值 |
|------|------|
| PubMed strict (Title/Abstract+gene/protein) | 40 |
| PubMed symbol_only | 60 |
| PubMed broad | 67 |

**关键文献**:
1. Palacios-Blanco I et al. (2024). "CDK phosphorylation of Sfr1 downregulates Rad51 function in late-meiotic homolog invasions." *EMBO J*. PMID: 39174851
2. Liang P et al. (2023). "Phosphoregulation of DNA repair via the Rad51 auxiliary factor Swi5-Sfr1." *J Biol Chem*. PMID: 37330173
3. Feng Y et al. (2013). "DNA homologous recombination factor SFR1 physically and functionally interacts with estrogen receptor alpha." *PLoS One*. PMID: 23874500
4. Wen Z et al. (2025). "Genetic insights into idiopathic pulmonary fibrosis: a multi-omics approach." *J Transl Med*. PMID: 40091050
5. Kuwabara N et al. (2010). "Expression, purification and crystallization of Swi5 and the Swi5-Sfr1 complex." *Acta Crystallogr F*. PMID: 20823543

**评价**: PubMed strict=40，高新颖性。研究主要集中于同源重组 DNA 修复和减数分裂。2013 年发现 ESR1 互作提示转录调控的潜在功能。

#### 3.4 三维结构分析

| 指标 | 数值 |
|------|------|
| UniProt 长度 | 245 aa |
| PDB 条数 | 0 |
| AlphaFold mean pLDDT | 66.9 |
| pLDDT >90 | 28.2% |
| pLDDT 70-90 | 16.7% |
| pLDDT 50-70 | 24.1% |
| pLDDT <50 | 31.0% |

**PAE 图**:

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/SFR1/SFR1-PAE.png]]

**评价**: 无 PDB 结构，仅 AlphaFold 预测。pLDDT 均值 66.9，31.0% 残基 <50。C 端区域预测置信度较低，可能为部分无序蛋白。SWI5-SFR1 复合体已有结晶报道 (2010)。

#### 3.5 结构域分析

| 来源 | 结构域 |
|------|------|
| InterPro | IPR042429 (Sfr1-like), IPR018468 (Sfr1) |
| Pfam | PF10376 (Sfr1) |

**染色质调控潜力分析**: SWI5-SFR1 复合体的组成部分，功能为 RAD51 介导的同源重组 DNA 修复辅助因子。非经典染色质调控结构域。但通过与 ESR1 (雌激素受体 alpha) 的物理和功能互作，可能参与转录调控。

#### 3.6 PPI 网络

**UniProt 记录互作** (实验级):

| Partner | 实验数 | 功能类别 |
|---------|--------|---------|
| SWI5 | 6 | HR repair cofactor |
| NMI | 6 | Interferon-inducible |
| RINT1 | 4 | ER/Golgi trafficking |
| RNF40 | 4 | Ubiquitin ligase |
| TFIP11 | 4 | Splicing factor |
| CEP70 | 3 | Centrosome |

**实验验证互作** (IntAct, physical association):

| Partner | 方法 | PMID | 功能类别 | 调控相关？ |
|---------|------|------|---------|-----------|
| SWI5 | two hybrid | 14663140 | HR repair | No |
| RAD51 | two hybrid | 14663140 | Recombinase | No |
| DTNBP1 | two hybrid | 17043677 | Dysbindin | No |

**STRING 预测互作** (combined score >0.5):

| Partner | Score | 实验分 | 功能类别 | 调控相关？ |
|---------|-------|--------|---------|-----------|
| SWI5 | 0.999 | 0.609 | HR cofactor | No |
| RAD51D | 0.923 | 0.045 | RAD51 paralog | No |
| RAD51C | 0.918 | 0.045 | RAD51 paralog | No |
| XRCC3 | 0.917 | 0.045 | RAD51 paralog | No |
| RAD51B | 0.916 | 0.045 | RAD51 paralog | No |
| RAD51 | 0.802 | 0.301 | Recombinase | No |
| SPO11 | 0.508 | 0 | Meiosis initiator | No |

**评价**: STRING 15 + IntAct 15 + UniProt 9。PPI 网络核心为 SWI5-SFR1-RAD51 同源重组 DNA 修复通路。UniProt 含 NMI (免疫)、RNF40 (泛素化)、TFIP11 (剪接) 和 CEP70 (中心体) 互作。另有文献报道的 ESR1 互作 (PMID: 23874500) 提示可能的转录调控功能。

#### 3.7 多库互证

| 维度 | 来源 | 结果 | 是否一致 |
|------|------|------|----------|
| 三维结构 | AlphaFold + PDB | PDB 0 (SWI5-Sfr1 复合体有结晶报道) | 部分 |
| 结构域 | UniProt/InterPro/Pfam | Sfr1 结构域多库一致 | 一致 |
| PPI 网络 | STRING + IntAct + UniProt | HR 修复网络多源互证 | 一致 |
| 核定位 | HPA/UniProt/GO | Nucleoli rim/Nucleoplasm 三源一致 | 一致 |

**互证加分明细**:
HPA IF (Supported) + UniProt 实验级 (ECO:0000269) + GO IDA 三源核定位一致 (+0.5)
**总计**: +0.5

### 4. 总体评价

**推荐等级**: ***oo (3/5)

**核心优势**:
1. 核定位高可信度，HPA + UniProt + GO 三源一致
2. 理想蛋白大小 (245 aa)，实验友好
3. ESR1 互作 (PMID: 23874500) 提示转录调控的潜在功能
4. 高新颖性 (PubMed strict=40)

**风险/不确定性**:
1. 主要功能为同源重组 DNA 修复，非经典转录调控因子
2. 无 DNA 结合结构域
3. 无 PDB 结构，AF pLDDT 中等 (66.9)
4. ESR1 互作的功能意义未深度研究

**下一步建议**:
- [ ] 验证 SFR1-ESR1 互作对下游靶基因（含 TE）转录的影响
- [ ] 解析 SWI5-SFR1 复合体晶体结构 (已有结晶报道)
- [ ] 探索 SFR1 在核仁的功能是否涉及 rDNA/TE 重复序列
- [ ] ChIP-seq 检测 SFR1 在基因组上的结合位点

### 5. 数据来源
- GeneCards: https://www.genecards.org/cgi-bin/carddisp.pl?gene=SFR1
- Protein Atlas: https://www.proteinatlas.org/ENSG00000156384-SFR1
- PubMed: https://pubmed.ncbi.nlm.nih.gov/?term=%22SFR1%22%5BTitle/Abstract%5D
- UniProt: https://www.uniprot.org/uniprot/Q86XK3
- STRING: https://string-db.org/network/9606.ENSG00000156384
- AlphaFold: https://alphafold.ebi.ac.uk/entry/Q86XK3

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/SFR1/IF_images/U-251MG_1.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/SFR1/IF_images/460_H10_1_blue_red_green.jpg]]

![[Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/SFR1/IF_images/460_H10_2_blue_red_green.jpg]]


#### PPI 网络
| Partner | Source | Score/Evidence |
|---|---|---|
| SWI5 | STRING | 0.999 |
| RAD51D | STRING | 0.923 |
| RAD51C | STRING | 0.918 |
| XRCC3 | STRING | 0.917 |
| RAD51B | STRING | 0.916 |
| P78932 | IntAct | psi-mi:"MI:0018"(two hybrid) |
| swi5 | IntAct | psi-mi:"MI:0018"(two hybrid) |
| rhp51 | IntAct | psi-mi:"MI:0018"(two hybrid) |

HPA IF 图像已本地嵌入。



**PAE 图像说明**: AlphaFold PAE 图像已重新获取并嵌入（见下方 PAE 图像修正块）；结构判断仍结合 pLDDT 与 PAE 综合判断。


![[/Users/quii/Documents/Obsidian Vault/Projects/TEreg-finding/protein-interested/detail/nucleus-cytoplasm/SFR1/SFR1-PAE.png]]

<!-- AF_PAE_REPAIR_START -->
**PAE 图像修正（2026-06-05）**: AlphaFold 提供 predicted aligned error 图像；此前“PAE 图像暂无数据”的表述为未获取/未嵌入导致。

![](https://alphafold.ebi.ac.uk/files/AF-Q86XK3-F1-predicted_aligned_error_v6.png)
<!-- AF_PAE_REPAIR_END -->
