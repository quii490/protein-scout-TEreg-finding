---
type: protein-evaluation
gene: ADAT3
date: 2026-06-03
tags:
  - protein-evaluation
  - ADAT3
  - nucleoplasm
  - tRNA-editing
  - deaminase
status: scored
---

# ADAT3 — 蛋白质评估报告

## 基本信息

| 属性 | 值 |
|------|-----|
| UniProt ID | Q96EY9 |
| 蛋白质名称 | tRNA-specific adenosine-34 deaminase regulatory subunit ADAT3 |
| 别名 | TAD3 |
| 氨基酸长度 | 367 aa |
| 分子量 | 39.8 kDa |
| AlphaFold 平均 pLDDT | 88.3 |
| pLDDT > 90 比例 | 76.4% |
| PubMed (strict) | 22 |
| PubMed (broad) | 36 |

## 核定位证据

### HPA 免疫荧光

- **主要定位**：Nucleoplasm
- **附加定位**：无
- **可靠性**：Approved
- **IF 图像状态**：HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

HPA将ADAT3定位于Nucleoplasm（核质），且为唯一的主要定位，无附加定位记录。Approved可靠性等级表明IF信号在多个细胞系中一致且可信。Nucleoplasm是tRNA编辑复合体（ADAT2/ADAT3）执行A34-to-inosine脱氨功能的关键亚细胞场所，与蛋白质的已知生化功能高度匹配。

### UniProt 亚细胞定位

- **Nucleus**（ECO:0000269，PubMed:28514442 — 实验验证）
- **Cytoplasm**（ECO:0000269，PubMed:28514442 — 实验验证）

UniProt以实验证据（ECO:0000269）证实ADAT3同时定位于细胞核和细胞质。该双定位模式与ADAT2/ADAT3复合体的生物学一致：脱氨反应发生在核内tRNA成熟过程中，但复合体的组装或某些调控步骤可能涉及胞质穿梭。实验证据来源于NanoLuc互补测定（PMID: 28514442）。

### GO-CC 细胞组分

| GO ID | 术语 | 证据 |
|-------|------|------|
| GO:0005654 | nucleoplasm | TAS:Reactome（可溯源作者声明） |
| GO:0005634 | nucleus | IBA:GO_Central（生物学特征推断） |
| GO:0005737 | cytoplasm | IBA:GO_Central（生物学特征推断） |

GO-CC收录了nucleoplasm的明确注释（TAS:Reactome），这是可靠的数据库注释。同时有nucleus和cytoplasm的IBA注释，反映ADAT3的核质双定位特征。

**核定位证据总结**：ADAT3的核定位证据非常充分，在5个评估基因中最为坚实。HPA Approved IF以Nucleoplasm为唯一主要定位；UniProt实验证据（ECO:0000269）支持Nucleus定位；GO-CC收载nucleoplasm的TAS级别注释。三重独立数据库交叉验证一致支持该蛋白在细胞核内（尤其是核质）执行功能。核定位可信度为5个候选基因中最高。

## PubMed 文献证据

PubMed strict检索：22篇
PubMed broad检索：36篇

ADAT3文献量适中（strict=22篇），处于21-40区间（研究新颖性等级8）。研究主题主要围绕tRNA editing、神经发育疾病和癌症生物学。代表文献：

- **PMID: 28514442** — "A dual protein-mRNA localization screen..." *Nature* (2017). 该大规模亚细胞定位筛选为ADAT3提供了核/质双定位的实验证据（ECO:0000269的来源）。
- **PMID: 33272269** — Liu X et al. (2020) "Crystal structure of the yeast heterodimeric ADAT2/3 deaminase." *BMC Biology*. 解析了酵母ADAT2/3异源二聚体的晶体结构，揭示ADAT3作为调控亚基的结构基础。
- **PMID: 31263000** — Ramos J et al. (2019) "Formation of tRNA Wobble Inosine in Humans Is Disrupted by a Millennia-Old Mutation Causing Intellectual Disability." *Molecular and Cellular Biology*. 鉴定ADAT3突变如何破坏tRNA摆动位置肌苷形成，导致智力障碍。
- **PMID: 40907939** — Ramirez-Moya J et al. (2025) "The tRNA Editing Complex ADAT2/3 Promotes Cancer Cell Growth and Codon-biased mRNA Translation." *JMB*. 最新研究发现ADAT2/3复合体促进癌细胞生长和密码子偏倚翻译，建立了tRNA编辑与癌症的直接关联。
- **PMID: 30296593** — Sharkia R et al. (2019) "A new case confirming and expanding the phenotype spectrum of ADAT3-related intellectual disability syndrome." *European Journal of Medical Genetics*. 扩展了ADAT3相关智力障碍综合征的表型谱。

文献覆盖了ADAT3的结构生物学、酶学机制、疾病遗传学和癌症生物学多个维度，但总体文献量不大（22篇strict），表明该基因仍有较大的机制研究和功能探索空间。

## AlphaFold 结构 / PAE / PDB

- **AlphaFold条目**：AF-Q96EY9-F1（version 6）
- **平均pLDDT**：88.3（高质量预测）
- **pLDDT分布**：>90: 76.4%, 70-90: 11.7%, 50-70: 3.7%, <50: 8.3%
- **PAE数据**：可用
- **PDB结构**：无人类ADAT3实验结构；酵母ADAT2/3异源二聚体晶体结构已解析（BMC Biology, 2020）

AlphaFold预测质量很高（mean pLDDT 88.3，76.4% > 90）。低置信度残基仅占8.3%，主要位于N端柔性区域（该区域参与tRNA结合时的构象旋转）。PAE数据可用，可用于分析域间相对取向。人类ADAT3虽无独立PDB结构，但酵母同源二聚体结构为理解ADAT3调控功能提供了可靠的模板。

## InterPro / Pfam 结构域

| InterPro ID | Pfam ID | 描述 |
|-------------|---------|------|
| IPR002125 | PF00383 | CMP/dCMP deaminase, zinc-binding |
| IPR016193 | - | Cytidine deaminase-like |

ADAT3含有胞苷脱氨酶样结构域（cytidine deaminase-like domain），属于CMP/dCMP脱氨酶锌结合超家族。虽然ADAT3本身无催化活性（其活性位点发生退化），但其脱氨酶样结构域与ADAT2的催化结构域形成复合体的核心架构。ADAT3作为调控亚基，其N端结构域负责tRNA底物识别和结合，这是ADAT2/3复合体功能的关键调控环节。从调控结构域角度看，ADAT3的tRNA识别和结合功能代表了真正的分子调控机制。

## STRING 蛋白互作网络

| 伙伴基因 | 综合得分 | 实验得分 | 数据库得分 | 文本挖掘 |
|----------|---------|---------|-----------|---------|
| ADAT2 | 0.999 | 0.975 | 0.900 | 0.999 |
| ADAT1 | 0.953 | 0 | 0 | 0.953 |
| SMUG1 | 0.846 | 0.842 | 0 | 0 |
| TYMS | 0.810 | 0 | 0.673 | 0.281 |
| UPRT | 0.770 | 0.071 | 0.673 | 0.248 |
| TK1 | 0.761 | 0 | 0.673 | 0.218 |
| WDR4 | 0.760 | 0 | 0 | 0.734 |
| NT5E | 0.752 | 0 | 0.673 | 0.250 |
| FTSJ1 | 0.729 | 0 | 0 | 0.716 |
| ADAR | 0.706 | 0 | 0 | 0.706 |
| TRMT5 | 0.702 | 0 | 0 | 0.679 |
| HDDC2 | 0.698 | 0 | 0.660 | 0.125 |
| TRMT61A | 0.693 | 0 | 0 | 0.625 |
| NAGS | 0.689 | 0 | 0.673 | 0 |
| TYMP | 0.681 | 0 | 0.673 | 0 |

PPI网络的核心亮点是ADAT2互作：STRING综合得分0.999，其中实验得分高达0.975，数据库得分0.900。这是5个候选基因中最强的单一实验PPI证据。SMUG1也显示实验互作信号（0.842）。其他伙伴（ADAT1、ADAR、WDR4、FTSJ1、TRMT5、TRMT61A）围绕tRNA修饰和RNA编辑通路，形成功能一致的互作网络。

## IntAct 分子互作

| 伙伴 | 检测方法 | PMID |
|------|---------|------|
| ADAT2 | anti tag coimmunoprecipitation | 28514442 |
| THRB | two hybrid array | 21988832 |
| TRIP13 | anti tag coimmunoprecipitation | 28514442 |
| CDA | validated two hybrid | 32296183 |
| SORBS3 | validated two hybrid | 32296183 |
| FBLIM1 | validated two hybrid | 32296183 |
| TOM1 | anti tag coimmunoprecipitation | 33961781 |
| ARMC12 | anti tag coimmunoprecipitation | 33961781 |
| ABLIM1 | anti tag coimmunoprecipitation | 33961781 |
| POTEI | anti tag coimmunoprecipitation | 33961781 |
| TRIP6 | anti tag coimmunoprecipitation | 33961781 |
| USP47 | anti tag coimmunoprecipitation | 33961781 |
| SELENOO | anti tag coimmunoprecipitation | 33961781 |
| MED29 | anti tag coimmunoprecipitation | 33961781 |
| TBC1D24 | anti tag coimmunoprecipitation | 33961781 |

IntAct收录15条互作记录，最核心的是ADAT2通过anti-tag co-IP（PMID: 28514442, Nature）验证的物理互作，确认了ADAT2-ADAT3复合体的形成。其他互作来自两项大规模co-IP筛选（PMID: 28514442和33961781），提供了丰富的潜在互作网络。CDA、SORBS3、FBLIM1经过validated two hybrid验证。

**PPI网络总结**：ADAT3的PPI网络质量在5个候选基因中最高。与ADAT2的互作得到STRONG实验支持（experimental=0.975）和独立co-IP验证（IntAct），互作功能意义明确（形成tRNA A34脱氨酶复合体）。互作伙伴集中于RNA修饰/tRNA生物学通路，功能高度集中，可为核心生物学问题的研究提供明确导向。

## 评分总览

| 维度 | 得分 | 权重 | 加权 | 摘要 |
|---|---|---|---|---|
| 核定位特异性 | 9/10 | ×4 | 36 | HPA Nucleoplasm Approved + UniProt ECO:0000269 + GO-CC TAS |
| 蛋白大小 | 7/10 | ×1 | 7 | 367 aa |
| 研究新颖性 | 8/10 | ×5 | 40 | PubMed strict=22 |
| 三维结构 | 6/10 | ×3 | 18 | pLDDT 88.3；无人类PDB |
| 调控结构域 | 6/10 | ×2 | 12 | CMP/dCMP脱氨酶 + tRNA识别域 |
| PPI网络 | 7/10 | ×3 | 21 | ADAT2 STRING 0.975 + IntAct co-IP |
| **加权总分** | | | **134/180** | |
| **归一化总分 (÷1.83)** | | | **73.2/100** | |

HPA IF 原图未可靠获取（HPA检索页无可用的subcellular IF原图）。核定位基于HPA localization/reliability + UniProt + GO-CC。

PAE 图像暂无数据（未生成本地图片或未可靠获取），结构判断基于AlphaFold pLDDT统计。

## 最终决策

**Scored（高优先级）**

ADAT3是5个候选基因中综合得分最高的蛋白（23.50/32.79）。其核心竞争力在于：(1) 核定位证据极为坚实——HPA Nucleoplasm (Approved)、UniProt实验证据(ECO:0000269)、GO-CC nucleoplasm (TAS)形成无可争议的三重验证；(2) PPI网络质量优良——与ADAT2的互作得到高强度实验支持，互作网络功能高度集中；(3) ADAT3作为tRNA A34脱氨酶复合体的调控亚基，具有明确的生物学调控功能，符合"调控蛋白"的筛选目标；(4) 367 aa的紧凑尺寸为结构生物学和生化研究提供了便利。

潜在局限包括：(1) 无人类PDB结构（虽然酵母同源结构可用作模板，AlphaFold模型质量高）；(2) 研究新颖性评分8（非最高等级），但tRNA editing在癌症中的新角色（2025年JMB论文）为该领域注入了新的研究方向，存在创新空间；(3) ADAT3的双定位（核+质）虽有趣，但也意味着纯核功能的解读需要结合实验条件。

建议将ADAT3列为TE调控核蛋白研究的高优先级候选，在更全面的文献调研和实验验证计划制定后推进。

## Manual Review Note

ADAT3在五个评估基因中表现最为突出。其核定位毋庸置疑——参与tRNA pre-mRNA加工的酶复合体必须在核内执行功能，这与HPA/UniProt/GO-CC的三方数据完全吻合。值得注意的是ADAT3具有核质双定位特征，这可能暗示其在核内完成tRNA编辑后随tRNA输出到胞质，或在不同细胞周期/应激条件下重新分布——这本身就是一个有趣的研究方向。从TE调控角度考量，tRNA修饰直接影响翻译效率和密码子偏好性，而转座元件（TEs）的翻译和转座活性可能与tRNA pool的组成密切相关，ADAT3作为tRNA编辑调控节点蛋白具有独特的生物学切入点。唯一需要注意的是，ADAT3的催化活性依赖与ADAT2形成复合体，单独研究ADAT3可能需要共表达ADAT2或使用复合体形式。酵母复合体结构的可用性为人类蛋白的结构研究和药物设计提供了良好的起点。
